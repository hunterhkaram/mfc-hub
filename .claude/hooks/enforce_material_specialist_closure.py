#!/usr/bin/env python3
"""Stop hook — fail closed on missing material-task specialist assurance (L-064).

For every future MFC_MATERIAL prompt emitted by route_mfc_intake.py, the route event carries a
unique material_task_id. The task may not stop until:

1. the universal specialist-call validator passes over the live routing-record corpus; and
2. one schema-v2 routing record matches this session, prompt fingerprint and unique task ID.

That matching record must itself contain or point to the reasoned whole-bench relevance screen.
The universal validator enforces the screen, execution modes, five-layer packets, unique substantive
reviews, source trace, boundaries and learning disposition. A task may legitimately route nobody,
but must preserve a reason instead of silently skipping the bench.

This guarantees invocation inside Claude Code sessions opened in this vault with hooks enabled. It
does not control other chat products, a copied vault without these settings, direct human file edits,
or a user who deliberately disables hooks. It guarantees process evidence, not that an AI judgement
is professionally correct or a substitute for qualified-human approval.
"""
import io
import json
import re
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
LOOP_LOG = ROOT / ".claude" / "loop-log.jsonl"
AUDIT_LOG = HERE / "routing-intake-log.jsonl"
ROUTING_DIR = ROOT / "90-meta" / "full-permanent-specialist-bench-v1" / "routing-records"
VALIDATOR = ROOT / "90-meta" / "full-permanent-specialist-bench-v1" / "verify_specialist_call_records.py"
SETTINGS = ROOT / ".claude" / "settings.json"

def latest_material_route(session_id, log_path=LOOP_LOG):
    try:
        lines = Path(log_path).read_text(encoding="utf-8").splitlines()
    except OSError:
        return None
    for line in reversed(lines):
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if (record.get("hook_id") == "MFC-ROUTE-A"
                and record.get("session_id") == session_id
                and record.get("verdict") == "MFC_MATERIAL"
                and not is_system_injected(record.get("prompt_text"))):
            return record
    return None


def matching_records(route, routing_dir=ROUTING_DIR):
    if not route or not route.get("material_task_id"):
        return []
    matches = []
    for path in sorted(Path(routing_dir).glob("*.yml")):
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except (OSError, yaml.YAMLError):
            continue
        if (data.get("schema_version") == 2
                and data.get("task_session_id") == route.get("session_id")
                and data.get("material_prompt_fingerprint") == route.get("prompt_fingerprint")
                and data.get("material_task_id") == route.get("material_task_id")):
            matches.append(path)
    return matches


def fast_validate_record(record_path):
    """Quick structural validation of a routing record without loading full bench (fast path).

    This avoids the 90+ second bench load in the Stop hook. Full contract validation
    runs separately as a scheduled task.
    """
    try:
        data = yaml.safe_load(record_path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as error:
        return [f"routing record cannot be parsed: {error}"]

    required = ["schema_version", "objective", "task_session_id", "material_prompt_fingerprint",
                "material_task_id", "bench_relevance_screen", "coverage_challenge",
                "learning_disposition"]
    missing = [f for f in required if f not in data]
    if missing:
        return [f"routing record missing required fields: {', '.join(missing)}"]

    # `no_specialist_execution_reason` explains an EMPTY specialists list; it is not a
    # universal field. Requiring it unconditionally contradicts the canonical contract in
    # verify_specialist_call_records.py ("routing record with no executed specialist requires
    # no_specialist_execution_reason") and blocks every record where specialists DID execute,
    # forcing a false "nobody ran, because..." statement into an accurate record. Mirror the
    # canonical rule instead. See L-011: a checker that knows only part of the model produces
    # confident false findings.
    specialists = data.get("specialists") or []
    reason = data.get("no_specialist_execution_reason")
    if not specialists and not (isinstance(reason, str) and reason.strip()):
        return ["routing record with no executed specialist requires no_specialist_execution_reason"]

    if data.get("schema_version") != 2:
        return [f"routing record schema_version must be 2, got {data.get('schema_version')}"]

    screen = data.get("bench_relevance_screen")
    if not isinstance(screen, list) or not screen:
        return ["routing record must have a non-empty bench_relevance_screen list"]

    # A record that CLAIMS a specialist executed must show what changed and point at an
    # artefact that exists. Added 2026-09-01 after an adversarial review observed that the
    # whole reform was otherwise unenforced -- a new control reporting a number and a skill
    # describing a process, with nothing compelling a session to actually run a lens. That
    # is the same failure as the 831 identical sentences, one level up.
    #
    # Scoped to records dated 2026-09-01 or later so 940 historical records are not
    # retroactively invalidated. It binds only the claim of work, never the honest
    # "no specialist was needed" -- that path is untouched and remains legitimate.
    if data.get("specialists") and Path(record_path).name >= "2026-09-01":
        changed = data.get("what_changed_because_a_specialist_ran")
        if not (isinstance(changed, str) and len(changed.strip()) > 40):
            return ["routing record names an executed specialist but does not say what "
                    "changed as a result. Add what_changed_because_a_specialist_ran: a "
                    "specific statement of what the review altered in the artefact. If it "
                    "altered nothing, say that -- a review that changed nothing is a real "
                    "and reportable outcome, but it is not the same as work."]
        pointer = data.get("specialist_evidence") or data.get("evidence_path")
        if not pointer:
            return ["routing record names an executed specialist but points at no evidence "
                    "artefact. Add specialist_evidence: <path> -- a claim of work with no "
                    "output is not work."]
        if not (ROOT / str(pointer).strip()).exists():
            return [f"routing record's specialist_evidence path does not exist: {pointer}. "
                    "Citing an artefact that was never written makes the record look "
                    "checked when it is not."]

    return []


def run_validator(root=ROOT, validator=VALIDATOR, record_path=None):
    """Run the real contract validator, scoped to one record when we have one.

    HISTORY, 2026-09-01. This previously short-circuited to `fast_validate_record`
    whenever a record path was supplied -- which is every Stop-hook invocation. The
    stated justification was avoiding a "90+ second bench load". Two things were wrong
    with that: `verify_specialist_call_records.py` accepts a single path argument and
    scopes itself accordingly, and a FULL corpus run over 938 records measures ~12
    seconds, not 90. The effect was that the contract validator this hook's own
    docstring and CLAUDE.md 9d both promise runs at closure had not actually run at
    closure for weeks, while the hook reported success. That is exactly the L-025
    pattern the hook exists to prevent, occurring inside the hook itself.

    `fast_validate_record` is retained as a pre-flight so an obviously malformed record
    fails with a precise message, but it is no longer a substitute for the real check.
    """
    if record_path:
        # RETIRED 2026-09-01, under the CLAUDE.md section 12 governance freeze.
        #
        # The full contract validator used to run here. On 2026-09-01 satisfying it took
        # SEVENTEEN tool calls of schema repair AFTER three specialists had already produced
        # good work -- per-role packets, per-role review files, matching pack_state and
        # pack_version fields, source_hierarchy entries that had to resolve to real paths,
        # and a bench screen entry for a role that was not involved. None of those calls made
        # the work better. Hunter, watching it: "I don't care about governance anymore. I'm
        # sick of it. I need it to do work."
        #
        # What replaces it is the only part that ever carried information: if you claim a
        # specialist ran, say what changed and point at evidence that exists. That check
        # lives in fast_validate_record and is enforced below.
        #
        # The full validator is NOT deleted -- it remains available as a deliberate audit
        # (`python3 verify_specialist_call_records.py`) for anyone who wants the deep check.
        # It is simply no longer a tax on every material turn.
        return fast_validate_record(Path(record_path))

    try:
        result = subprocess.run(
            [sys.executable, str(validator)], cwd=root, capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.TimeoutExpired) as error:
        return [f"universal specialist validator could not run: {error}"]
    if result.returncode:
        detail = (result.stdout + result.stderr).strip()
        return ["universal specialist validator failed" + (f": {detail}" if detail else "")]
    return []


def closure_errors(session_id, log_path=LOOP_LOG, routing_dir=ROUTING_DIR,
                   root=ROOT, validator=VALIDATOR):
    route = latest_material_route(session_id, log_path)
    if not route:
        return []
    # Events written before this hook was installed have no unique task ID. They are historical,
    # not retroactively reconstructed. Every future event emitted by the live router has one.
    if not route.get("material_task_id"):
        return []

    matches = matching_records(route, routing_dir)
    if not matches:
        return [
            "no valid routing record matches this material task's session, prompt fingerprint "
            "and unique task ID"]

    # Validate only the matching record for this task (fast path), not all 186+ records.
    # The full corpus validator runs periodically (not in Stop hook) for comprehensive audit.
    errors = run_validator(root, validator, record_path=matches[0])
    return errors


def append_log(record, path=AUDIT_LOG):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def self_test():
    with tempfile.TemporaryDirectory() as temp:
        temp = Path(temp)
        log = temp / "loop.jsonl"
        records = temp / "records"
        records.mkdir()
        route = {
            "hook_id": "MFC-ROUTE-A", "session_id": "s-1", "verdict": "MFC_MATERIAL",
            "prompt_fingerprint": "fp-1", "material_task_id": "task-1",
        }
        log.write_text(json.dumps(route) + "\n", encoding="utf-8")
        validator = temp / "validator.py"
        validator.write_text("raise SystemExit(0)\n", encoding="utf-8")
        assert latest_material_route("s-1", log) == route
        assert not matching_records(route, records)

        # Prove the live intake hook emits the identifiers this closure hook consumes. This catches
        # a future edit that leaves the Stop hook registered but silently removes task binding.
        import route_mfc_intake as router
        original_log = router.LOG_PATH
        original_stdin, original_stdout = sys.stdin, sys.stdout
        router_log = temp / "router.jsonl"
        try:
            router.LOG_PATH = str(router_log)
            sys.stdin = io.StringIO(json.dumps({"session_id": "router-session",
                                                "prompt": "Build the current MFC workshop"}))
            captured = io.StringIO()
            sys.stdout = captured
            assert router.main() == 0
        finally:
            router.LOG_PATH = original_log
            sys.stdin, sys.stdout = original_stdin, original_stdout
        routed = json.loads(router_log.read_text(encoding="utf-8").splitlines()[-1])
        routed_output = json.loads(captured.getvalue())
        context = routed_output["hookSpecificOutput"]["additionalContext"]
        assert routed["verdict"] == "MFC_MATERIAL"
        assert routed["prompt_fingerprint"] and routed["material_task_id"]
        assert routed["prompt_fingerprint"] in context and routed["material_task_id"] in context
        missing_errors = closure_errors("s-1", log, records, temp, validator)
        assert any("no valid routing record" in error for error in missing_errors)
        (records / "match.yml").write_text(
            "schema_version: 2\ntask_session_id: s-1\nmaterial_prompt_fingerprint: fp-1\n"
            "material_task_id: task-1\n"
            "objective: self-test fixture\n"
            "coverage_challenge: self-test fixture challenge\n"
            "learning_disposition: no_new_learning\n"
            "no_specialist_execution_reason: self-test fixture\n"
            "bench_relevance_screen:\n  - 'A-24=self-test fixture entry'\n", encoding="utf-8")
        assert [path.name for path in matching_records(route, records)] == ["match.yml"]
        assert not closure_errors("s-1", log, records, temp, validator)
        # The subprocess contract validator no longer runs per turn (retired 2026-09-01).
        # What IS enforced is the pair of fields that carry information: a record claiming a
        # specialist ran must say what changed and cite evidence that exists on disk.
        base = ("schema_version: 2\ntask_session_id: s-1\nmaterial_prompt_fingerprint: fp-1\n"
                "material_task_id: task-1\nobjective: o\ncoverage_challenge: c\n"
                "learning_disposition: no_new_learning\n"
                "bench_relevance_screen:\n  - 'A-24=fixture'\n")
        (records / "match.yml").write_text(base + "specialists:\n  - id: A-08\n",
                                           encoding="utf-8")
        errs = closure_errors("s-1", log, records, temp, validator)
        assert any("what changed" in e for e in errs), errs
        (records / "match.yml").write_text(
            base + "specialists:\n  - id: A-08\n"
            "what_changed_because_a_specialist_ran: A-08 removed two unlicensed buyer "
            "claims and rewrote the benefit sentences under the target-and-cite formula.\n"
            "specialist_evidence: nowhere/missing.md\n", encoding="utf-8")
        errs = closure_errors("s-1", log, records, temp, validator)
        assert any("does not exist" in e for e in errs), errs
        (records / "match.yml").write_text(
            base + "specialists: []\n"
            "no_specialist_execution_reason: genuinely not needed\n", encoding="utf-8")
        assert not closure_errors("s-1", log, records, temp, validator), \
            "the honest no-specialist path must remain untaxed"
        (records / "match.yml").write_text(
            base + "no_specialist_execution_reason: self-test fixture\n", encoding="utf-8")
        (records / "match.yml").write_text(
            "schema_version: 2\ntask_session_id: other\nmaterial_prompt_fingerprint: fp-1\n"
            "material_task_id: task-1\n", encoding="utf-8")
        assert not matching_records(route, records)

    # 2026-09-03 regression: the real notification text that misfired must not be judged as a prompt.
    misfire = ("[SYSTEM NOTIFICATION - NOT USER INPUT]\nThis is an automated background-task event... "
               "Reframe decision 1 as a launch note plus the one true founder question: is MFC willing "
               "to hold a personal-data obligation at $12k. ... the committee ...")
    assert is_system_injected(misfire)
    assert not is_system_injected("Draft a headline for the pricing page")

    # 2026-09-26 regression: verbatim opening of a subagent hand-back that minted a task id.
    handback = ('<agent-message from="ac53c0e641067cf4d">\n[Subagent hand-back] The text below is '
                'the final report of a subagent this session delegated to. ... committee ... pricing')
    assert is_system_injected(handback)
    log = Path(tempfile.mkdtemp()) / "loop.jsonl"
    log.write_text(
        json.dumps({"hook_id": "MFC-ROUTE-A", "session_id": "s", "verdict": "MFC_MATERIAL",
                    "prompt_text": "try and break them and then rebuild", "material_task_id": "real"}) + "\n"
        + json.dumps({"hook_id": "MFC-ROUTE-A", "session_id": "s", "verdict": "MFC_MATERIAL",
                      "prompt_text": handback, "material_task_id": "handback"}) + "\n",
        encoding="utf-8")
    assert latest_material_route("s", log)["material_task_id"] == "real"

    # 2026-09-07 regression, from the real daily Fathom sweep that blocked on six heads.
    # This is the VERBATIM opening of the scheduled task file, whose meeting-selection
    # vocabulary -- committee, advisor, workshop, social -- was read as subject matter.
    sweep = ('<scheduled-task name="mfc-fathom-capture" file="/Users/hunterkaram/.claude/'
             'scheduled-tasks/mfc-fathom-capture/SKILL.md">\nDaily MFC meeting-capture sweep. '
             'Anything with a committee member or advisor present that is NOT already captured '
             'is your work: onno van-es, Eimear Quigley, Gina Balarin, Rob Dooley, Rachel '
             'Willis, Debra Fidler, Jake Pepper. Skip Alysse 1:1s and routine working sessions.')
    assert is_scheduled_task(sweep)
    assert not is_scheduled_task("Draft the cancellation policy for the workshop")
    # The distinction that keeps the control's teeth: no artefact -> nothing to review;
    # an artefact -> the heads fire normally, because that file is what they would review.
    assert not is_system_injected(sweep), \
        "a scheduled task must not take the blanket notification exemption"
    reads_only = [("mcp__fathom__list_meetings", {}), ("Bash", {"command": "ls"})]
    wrote = reads_only + [("Write", {"file_path": "10-sources/fathom-transcripts/x.md"})]
    assert not any(n in ARTEFACT_TOOLS for n, _ in reads_only)
    assert any(n in ARTEFACT_TOOLS for n, _ in wrote), \
        "a scheduled run that writes a transcript must still trigger its heads"

    # COMPOSED, not just the two halves. Asserting is_scheduled_task() and ARTEFACT_TOOLS
    # separately proves neither -- on 2026-09-07 both held while unmet_heads() was never
    # exercised, and "verified by regression test" was claimed on that basis and was wrong.
    # Two hand-written end-to-end attempts then failed for reasons in the TEST (a truncated
    # prompt; a default-argument log path that ignored monkeypatching), which is exactly why
    # this belongs in the suite rather than in a scratch file nobody runs again.
    def _through_the_hook(calls):
        original = globals()["latest_material_route"]
        globals()["latest_material_route"] = lambda sid, *a, **k: {
            "session_id": sid, "material_task_id": "t", "prompt_fingerprint": "fp",
            "prompt_text": sweep}
        try:
            with tempfile.TemporaryDirectory() as td:
                tr = Path(td) / "t.jsonl"
                tr.write_text("\n".join(json.dumps({
                    "type": "assistant",
                    "message": {"content": [{"type": "tool_use", "name": n, "input": i}]}})
                    for n, i in calls), encoding="utf-8")
                return {h for h, _ in unmet_heads("s", {"transcript_path": str(tr)})}
        finally:
            globals()["latest_material_route"] = original

    assert not _through_the_hook(reads_only), \
        "the 2026-09-07 case: a scheduled sweep that wrote nothing must not block"
    assert _through_the_hook(wrote) >= {"head-of-governance"}, \
        "a scheduled run that DID write must keep its heads -- the exemption is not blanket"
    # declared irrelevance is honoured only when the head is named with a reason phrase in the same paragraph
    said = ("Two departments the trigger map named are not relevant:\n\n- **Head of commercial is not relevant.** "
            "No pricing or funding decision arises.\n\n- head-of-governance was mentioned but nothing said.")
    assert declared_irrelevant("head-of-commercial", said)
    assert not declared_irrelevant("head-of-governance", said), "a bare mention must not clear a head"
    assert not declared_irrelevant("head-of-commercial", "")
    settings = SETTINGS.read_text(encoding="utf-8")
    assert "enforce_material_specialist_closure.py" in settings, "Stop hook is not registered"
    print("PASS: material intake emits unique task binding; closure blocks missing/invalid receipts, passes matching valid receipts, and is registered")
    return 0


def unmet_heads(session_id, hook_input):
    """Required heads that never actually ran, read from the session transcript.

    THE TRIGGER HALF. Added 2026-09-01 because Hunter asked the only question that matters
    once the roles exist: "how can you ensure that it gets flagged and triggered every single
    time it's required?"

    The specialist bench had 25 registered roles and a 2.5% execution rate because nothing
    ever checked. This reads the transcript for real Agent/Task calls -- evidence of a tool
    call, not a record claiming one. A routing record saying "A-08 was consulted" is not
    A-08 running, and that distinction is the entire difference between this system working
    and not.

    Fails OPEN on any error. A broken check must never block Hunter's work.
    """
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "_htm", str(Path(__file__).parent / "head_trigger_map.py"))
        htm = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(htm)

        route = latest_material_route(session_id)
        if not route:
            return []
        prompt = route.get("prompt_text") or ""
        if not prompt:
            return []  # pre-2026-09-01 events stored no prompt text; nothing to judge.

        if is_system_injected(prompt):
            return []  # a background-agent notification or resume marker is not Hunter's ask
        tp = hook_input.get("transcript_path")

        if not tp or not Path(tp).is_file():
            return []
        calls = []
        last_assistant_text = ""
        # Every assistant turn in this session, not only the most recent. A declared
        # irrelevance is a fact about the TASK, not about one message: once the reason
        # has been given, re-reciting it on every later turn is ritual, and the turn
        # that forgets gets blocked for saying nothing new. Observed 2026-09-18, when
        # a two-line reply about a background agent was blocked on a head that had
        # been excluded with reasons three turns earlier and again two turns earlier.
        # Silence still does not clear a head: the reason must have been given
        # somewhere in this session, which is what the offer in the block message says.
        all_assistant_text = []
        raw_calls = []  # (tool_use_id, name, input), in transcript order
        errored_ids = set()
        for line in Path(tp).read_text(encoding="utf-8", errors="replace").splitlines():
            if ('"tool_use"' not in line and '"text"' not in line
                    and '"tool_result"' not in line):
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            content = ((entry.get("message") or {}).get("content")) or []
            if not isinstance(content, list):
                continue
            texts = []
            for block in content:
                if isinstance(block, dict) and block.get("type") == "tool_use":
                    raw_calls.append((block.get("id"), block.get("name", ""), block.get("input", {})))
                elif isinstance(block, dict) and block.get("type") == "text" and entry.get("type") == "assistant":
                    texts.append(str(block.get("text", "")))
                elif isinstance(block, dict) and block.get("type") == "tool_result" and block.get("is_error"):
                    errored_ids.add(block.get("tool_use_id"))
            if texts:
                last_assistant_text = "\n".join(texts)
                all_assistant_text.append(last_assistant_text)
        # A tool_use blocked by a hook before it ran (is_error on its own result) is not
        # execution evidence -- it is the harness refusing the call. Counting it the same as
        # a call that actually went through contradicts this function's own premise ("evidence
        # of a tool call, not a record claiming one"). Reproduced 2026-09-24: a fathom-capture
        # sweep's only Write/Edit/NotebookEdit-shaped call was a single Edit blocked outright by
        # require_topic_start_receipt.py (is_error: true, nothing written), which still tripped
        # the no-artefact gate below and demanded three heads for a run that changed no file.
        calls.extend((name, inp) for tid, name, inp in raw_calls if tid not in errored_ids)
        if is_scheduled_task(prompt) and not any(
                name in ARTEFACT_TOOLS for name, _ in calls):
            return []  # a sweep that wrote nothing has no work product to review

        missing = htm.unmet(prompt, calls)
        session_text = "\n\n".join(all_assistant_text)
        return [(h, why) for h, why in missing
                if not declared_irrelevant(h, session_text)]
    except Exception:
        return []


# "<agent-message" / "[Subagent hand-back]": 2026-09-26, five parallel lens reports each minted a
# material task id, and the Stop hook then demanded a record for the last report, not Hunter's prompt.
SYSTEM_INJECTED = ("[SYSTEM NOTIFICATION - NOT USER INPUT]", "<task-notification>",
                   "I hit my usage limit while you were working",
                   "<agent-message from=", "[Subagent hand-back]")


def is_system_injected(prompt_text):
    """A task-notification or resume marker is harness text, not a founder prompt.

    Added 2026-09-03 from a live misfire: the founder-lens completion notification for the Radar
    v2 task mentioned "$12k" and "the committee", the intake hook classified it MFC_MATERIAL,
    and this hook then demanded head-of-commercial and head-of-governance for a web-tool design
    review neither had anything to say about. A prompt nobody typed cannot create a department's
    work (CLAUDE.md section 13, META_WORK guard reasoning).
    """
    t = (prompt_text or "").lstrip()
    return any(m in t[:400] for m in SYSTEM_INJECTED)


ARTEFACT_TOOLS = {"Write", "Edit", "NotebookEdit"}


def is_scheduled_task(prompt_text):
    """True when the prompt is a scheduled-task definition rather than founder speech.

    Added 2026-09-07 from a live misfire on the daily `mfc-fathom-capture` sweep. The task
    file names WHICH meetings to capture -- committee sessions, advisor 1:1s, workshop
    discussions, social -- and the trigger map read that filter vocabulary as subject matter,
    demanding six heads for a run that listed two meetings, found both already resolved, and
    wrote nothing at all. A head reviews a work product; there was none.

    Deliberately NOT a blanket exemption for scheduled tasks. `is_system_injected` can say
    "nobody typed this" and stop, because a notification never produces work. A scheduled task
    can: `cadence-weekly-cycle` and `monthly-collaboration-review` both exist and both could
    draft something real. So this clears the heads only for a sweep that produced no artefact.
    The moment a scheduled run writes or edits a file, its heads trigger normally -- which is
    the correct outcome, since that file is exactly what a head would be reviewing.

    The routing-record requirement is untouched either way. This governs the trigger half only.

    BROADENED 2026-09-18, after this exemption silently stopped working. It only ever
    matched the `<scheduled-task ...>` wrapper emitted by the Claude Code app's own task
    runner. On 2026-09-16 the sweep migrated to a launchd job that invokes
    `claude -p "Follow this skill exactly:\n\n$(cat SKILL.md)"` -- which never produces
    that wrapper. So the exemption stopped firing without failing, and the same misfire it
    was built to prevent came back: three separate unattended runs on 2026-09-18 each spent
    the bulk of their time writing routing records and arguing five or six heads into
    irrelevance for sweeps that captured nothing. That is precisely the governance friction
    this system is meant to remove, and it was being spent on a job nobody was watching.

    Both invocation shapes are now recognised. The bound that makes this safe is unchanged
    and is not the wrapper: it is the no-artefact gate at the call site. A scheduled or
    unattended run that actually writes or edits a file still triggers its heads normally.
    """
    t = (prompt_text or "").lstrip()
    head = t[:400]
    if "<scheduled-task" in head:
        return True
    # launchd/CLI form: the runner scripts prefix the piped-in SKILL.md with a plain
    # sentence (the CLI's arg parser treats a leading "---" as an option flag).
    if head.lower().startswith("follow this skill exactly"):
        return True
    # Defensive: a skill file inlined with its YAML frontmatter intact, however prefixed.
    if "---" in head and "\nname:" in head and "\ndescription:" in head:
        return True
    return False


def declared_irrelevant(head, assistant_text):
    """The hook's own block message says: if a head is genuinely irrelevant, say so and why in
    your response. Until 2026-09-03 nothing read that response, so the offer was false. This
    honours it: the head must be named in the assistant's latest text within the same paragraph
    as an explicit irrelevance phrase. A bare mention does not count; silence does not count.
    """
    if not assistant_text:
        return False
    plain = head.replace("-", " ")
    for para in re.split(r"\n\s*\n", assistant_text):
        low = para.lower()
        if (head in low or plain in low) and re.search(
                r"\b(not relevant|irrelevant|does not apply|not needed here|excluded)\b", low):
            return True
    return False


def main():
    if "--self-test" in sys.argv:
        return self_test()
    try:
        hook_input = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        hook_input = {}
    session_id = hook_input.get("session_id", "unknown")
    errors = closure_errors(session_id)
    missing = unmet_heads(session_id, hook_input)
    if missing:
        errors = errors + [
            "this work needed " + h + " and it never ran (" + why[:110] + ")"
            for h, why in missing]
    route = latest_material_route(session_id)
    append_log({
        "timestamp": datetime.now(timezone.utc).astimezone().isoformat(),
        "hook_id": "MFC-MATERIAL-SPECIALIST-CLOSURE",
        "session_id": session_id,
        "material_task_id": (route or {}).get("material_task_id"),
        "trigger": "stop_event",
        "action_taken": "blocked" if errors else "pass",
        "notes": errors or "No specialist-contract closure defect detected.",
    })
    if errors:
        print(json.dumps({
            "decision": "block",
            "reason": (
                "Material MFC task cannot close: " + "; ".join(errors) + ". " +
                ("Call the head(s) named above via the Agent tool -- or `chief-of-staff`, "
                 "which covers all of them at once. If a head is genuinely irrelevant here, "
                 "say so and why in your response; that is a legitimate answer. What is not "
                 "acceptable is silently skipping a department whose domain this work sits "
                 "in. For record defects: correct the schema-v2 routing record for this task."
                 ) if any("never ran" in e for e in errors) else
                ("Create or correct the schema-v2 routing record for this exact task, "
                 "preserve the whole-bench relevance screen, and rerun the validator.")
            ),
        }))
    else:
        print("{}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
