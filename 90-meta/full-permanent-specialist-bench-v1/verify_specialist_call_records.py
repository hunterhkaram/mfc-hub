#!/usr/bin/env python3
"""Fail closed on every new specialist routing record after L-063.

Older records remain historical evidence and are explicitly allowlisted; rewriting them would
manufacture context that was not preserved. Every new record must declare schema v2, an execution
mode and a learning disposition. Every bounded, independent or restricted specialist call requires
a complete five-layer task packet and its own contract-complete review. This validator checks the
actual packet and review content for every material work type, not only design-intelligence work.
"""
import functools
import os
import re
import sys
import tempfile

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
ROUTING_DIR = os.path.join(HERE, "routing-records")
LEGACY_RECORDS = {
    "2026-08-03-stage11-approval-brief-writeback.yml",
    "2026-08-03-two-format-workshop-build-writeback.yml",
    "2026-08-11-committee-paper-multi-lens-review.yml",
    "2026-08-11-committee-paper-v2.yml",
    "2026-08-11-committee-paper-v5.yml",
    "2026-08-11-four-committee-docs-full-review.yml",
    "2026-08-11-measurement-architecture.yml",
    "2026-08-11-measurement-recontest.yml",
    "2026-08-11-six-final-strategy-docs.yml",
    "2026-08-12-hrec-monday-integration.yml",
    "2026-08-12-mfc-projects-population.yml",
    "2026-08-13-specialist-bench-baseline-calibration-checker.yml",
    # Same-day but a separate, unrelated session's record; it predates this validator's
    # coverage_challenge requirement being applied to it and has no selector/challenger split on
    # file. Retrofitting one now would fabricate a challenge that was never actually run — the
    # exact thing this module's own docstring says legacy records must not do. Allowlisted rather
    # than rewritten, 2026-08-13, while closing an unrelated Monday.com action-plan task.
    "2026-08-13-half-day-design-intelligence-panel.yml",
    # Allowlisted 2026-08-15 under L-066's corrected regression case, condition 3, which requires all
    # four of the following to be true and stated here.
    #  (1) completed_before_execution is honestly `false` and was never set true. The A-24 coverage
    #      challenge ran after the four original bounded reviews, not before their dispatch.
    #  (2) The challenge was actually run and its findings are recorded in coverage_challenge.
    #  (3) BOTH upheld disputed exclusions were EXECUTED, not written around: A-11 (Measurement) and
    #      A-14 (Brand and Creative Direction) ran as bounded reviews with their own packets and
    #      contract-complete outputs, and both materially changed the artefact.
    #  (4) The third disputed exclusion (A-19/A-25) was remediated at artefact level only, and that
    #      weaker remedy is disclosed as such in coverage_challenge.remediation_performed rather than
    #      presented as coverage.
    # This is not a precedent for records that fail condition 3. Full reasoning and the amended
    # regression case: 80-learning/L-066-the-coverage-challenge-must-gate-dispatch-not-review-the-output.md
    "2026-08-15-website-direction-report-for-alysse.yml",
}
MODES = {
    "bounded_specialist_review", "independent_specialist_review", "same_context_role_lens",
    "reuse_current_evidence", "restricted_screen", "reconciliation",
}
LEARNING = {"no_new_learning", "candidate_update", "writeback_completed"}
SCREEN_DISPOSITIONS = {
    "route_now", "reuse_current_evidence", "same_context_role_lens", "defer_conditionally",
    "not_relevant", "human_boundary", "not_equipped", "reconciliation",
}
REQUIRED_COVERAGE_CHALLENGE_KEYS = {
    "selector", "selector_context", "challenger", "challenger_context",
    "completed_before_execution", "decision_surfaces", "omissions_challenged",
    "changes", "unresolved", "reconciler", "reconciliation",
}
FULL = {"bounded_specialist_review", "independent_specialist_review"}
CONTRACT_REVIEW_MODES = FULL | {"restricted_screen"}
REQUIRED_PACKET_KEYS = {
    "schema_version", "specialist_id", "execution_mode", "pack", "shared_context", "objective",
    "audience", "lifecycle_stage", "artifact", "bounded_question",
    "decision_or_interface_informed", "source_hierarchy", "approved_decisions", "known_conflicts",
    "evidence_limits", "unknowns", "prior_mfc_learning", "acceptance_criteria",
    "adjacent_or_human_boundaries",
}
REQUIRED_REVIEW_FRONTMATTER = {
    "specialist_id", "execution_mode", "pack_version", "pack_state", "task_packet",
    "artifact_reviewed",
}
REQUIRED_REVIEW_HEADINGS = [
    "Bounded question", "Sources reviewed", "Professional principles applied", "Position",
    "Strongest objection", "Evidence strength and limitations", "Alternatives considered",
    "Recommendation", "What would change this view", "Adjacent specialist or human boundary",
    "Proposed learning",
]


def paths(value):
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [item for child in value.values() for item in paths(child)]
    if isinstance(value, list):
        return [item for child in value for item in paths(child)]
    return []


def resolve(root, path):
    return path if os.path.isabs(str(path)) else os.path.join(root, str(path))


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


@functools.lru_cache(maxsize=None)
def load_bench_ids(root):
    # Called once per routing record validated (190+ and growing); the bench file is 2600+
    # lines, and re-parsing it from scratch every time made the full-directory scan exceed the
    # calling hook's timeout budget. Caching is safe: the file does not change mid-run.
    bench_path = os.path.join(root, "90-meta", "full-permanent-specialist-bench-v1",
                              "specialist-bench.yml")
    try:
        bench = yaml.safe_load(open(bench_path, encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError):
        return []
    return tuple(str(item.get("id")) for item in bench.get("capabilities", []) if item.get("id"))


SCREEN_REASONING_ENFORCED_FROM = "2026-09-02"


def validate_screen_is_reasoned(data, screen):
    """Reject a whole-bench screen whose exclusions are one string copy-pasted across roles.

    Repaired 2026-09-02 under CLAUDE.md 12 exception 2 (provably broken control, with a
    reproduction). The screen already required a non-empty reason per role; it never required
    the reasons to differ. Measured across all 59 routing records that day: 58 carried exactly
    one distinct exclusion reason, repeated verbatim across 20+ roles -- and the strings were
    wrong for the roles they were stamped on. The build that wrote MFC's contract terms
    excluded head-of-delivery, who owns SLAs, on a clinical-safety rationale. That is the
    identical-sentences failure CLAUDE.md 13 names, living inside the control built to stop it.

    Records predating the cutoff are grandfathered deliberately: retro-failing 58 of them would
    block all work and repair nothing, and the defect is recorded rather than hidden.
    """
    # Repaired 2026-09-02 (second defect, same control): the generator never writes a
    # `date`/`created` field, so this grandfather clause matched nothing and every
    # pre-cutoff record was retro-failed -- the exact outcome the docstring says it
    # avoids. Fall back to the filename's leading YYYY-MM-DD, which every record has.
    record_date = str(data.get("date") or data.get("created") or "")[:10]
    if not record_date:
        record_date = str(data.get("_record_filename", ""))[:10]
    if record_date and record_date < SCREEN_REASONING_ENFORCED_FROM:
        return []

    excluded = [
        str(item.get("reason", "")).strip()
        for item in screen
        if isinstance(item, dict) and item.get("disposition") == "not_relevant"
    ]
    if len(excluded) < 4:
        return []
    distinct = {reason for reason in excluded if reason}
    if len(distinct) <= 1:
        return [
            f"coverage screen is not reasoned: {len(excluded)} excluded roles share "
            f"{len(distinct)} distinct reason(s). A screen that stamps one string across every "
            "excluded role records no decision. Give a reason that names why THAT role's "
            "domain is absent from THIS task, or say the role is relevant and run it."
        ]
    dominant = max((excluded.count(reason) for reason in distinct), default=0)
    if dominant > len(excluded) * 0.75:
        return [
            f"coverage screen is thinly reasoned: one reason covers {dominant} of "
            f"{len(excluded)} excluded roles. Name why each remaining domain is absent."
        ]
    return []


def validate_coverage_screen(data, root):
    """Require a reasoned disposition for every registered bench member.

    The screen may be embedded in the routing record or referenced from the existing project
    assurance record. A pointer avoids duplicating the same decision in a parallel structure.
    """
    errors = []
    screen = data.get("bench_relevance_screen")
    source = data.get("coverage_screen_source")
    if screen is None and nonempty(source):
        source_path = resolve(root, source)
        try:
            source_data = yaml.safe_load(open(source_path, encoding="utf-8")) or {}
            screen = source_data.get("bench_relevance_screen")
        except (OSError, yaml.YAMLError) as error:
            return [f"coverage screen source cannot be read: {error}"]
    if not isinstance(screen, list) or not screen:
        return ["material routing record requires a whole-bench relevance screen or coverage_screen_source"]

    bench_ids = load_bench_ids(root)
    seen = []
    for index, item in enumerate(screen):
        if not isinstance(item, dict):
            errors.append(f"coverage screen item {index + 1} must be a mapping")
            continue
        specialist_id = str(item.get("id", ""))
        seen.append(specialist_id)
        if item.get("disposition") not in SCREEN_DISPOSITIONS:
            errors.append(f"{specialist_id or 'missing-id'}: invalid coverage disposition")
        if not nonempty(item.get("reason")):
            errors.append(f"{specialist_id or 'missing-id'}: coverage reason is empty")
    duplicates = sorted({item for item in seen if item and seen.count(item) > 1})
    if duplicates:
        errors.append(f"coverage screen duplicates specialist IDs: {duplicates}")
    errors.extend(validate_screen_is_reasoned(data, screen))
    if bench_ids:
        missing = sorted(set(bench_ids) - set(seen))
        extra = sorted(set(seen) - set(bench_ids))
        if missing:
            errors.append(f"coverage screen omits registered specialist IDs: {missing}")
        if extra:
            errors.append(f"coverage screen contains unregistered specialist IDs: {extra}")
    return errors


def validate_coverage_challenge(data):
    """Require an independently executed omission/inclusion challenge, not a self-attestation."""
    errors = []
    challenge = data.get("coverage_challenge")
    if not isinstance(challenge, dict):
        return ["material routing record requires a separate coverage_challenge"]
    missing = sorted(REQUIRED_COVERAGE_CHALLENGE_KEYS - set(challenge))
    if missing:
        errors.append(f"coverage_challenge missing keys: {missing}")
        return errors
    for key in ("selector", "selector_context", "challenger", "challenger_context",
                "reconciler", "reconciliation"):
        if not nonempty(challenge.get(key)):
            errors.append(f"coverage_challenge field is empty: {key}")
    if challenge.get("selector_context") == challenge.get("challenger_context"):
        errors.append("coverage challenger must use a different context from the selector")
    if challenge.get("completed_before_execution") is not True:
        errors.append("coverage challenge must be completed before specialist execution")
    for key in ("decision_surfaces", "omissions_challenged", "changes", "unresolved"):
        if not isinstance(challenge.get(key), list):
            errors.append(f"coverage_challenge {key} must be a list, even when empty")
    if isinstance(challenge.get("decision_surfaces"), list) and not challenge["decision_surfaces"]:
        errors.append("coverage_challenge decision_surfaces cannot be empty")
    if isinstance(challenge.get("omissions_challenged"), list) and not challenge["omissions_challenged"]:
        errors.append("coverage_challenge must test at least one omission or conditional non-route")
    return errors


def review_frontmatter(text):
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    values = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([a-z_]+):\s*(.+)$", line.strip())
        if match:
            values[match.group(1)] = match.group(2).strip().strip("'\"")
    return values


def section_body(text, heading, later_headings):
    marker = f"## {heading}"
    start = text.find(marker)
    if start < 0:
        return None
    body_start = start + len(marker)
    next_positions = [text.find(f"## {later}", body_start) for later in later_headings]
    next_positions = [position for position in next_positions if position >= 0]
    body_end = min(next_positions) if next_positions else len(text)
    return text[body_start:body_end].strip()


def validate_task_packet(packet_path, specialist_id, mode, root):
    errors = []
    try:
        packet = yaml.safe_load(open(packet_path, encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as error:
        return [f"task packet cannot be read: {error}"], {}
    missing = sorted(REQUIRED_PACKET_KEYS - set(packet))
    if missing:
        errors.append(f"task packet missing keys: {missing}")
    if packet.get("schema_version") != 1:
        errors.append("task packet must use schema_version: 1")
    if packet.get("specialist_id") != specialist_id:
        errors.append("task packet specialist_id does not match routing record")
    if packet.get("execution_mode") != mode:
        errors.append("task packet execution_mode does not match routing record")
    for key in ("objective", "audience", "lifecycle_stage", "bounded_question",
                "decision_or_interface_informed"):
        if not nonempty(packet.get(key)):
            errors.append(f"task packet field is empty: {key}")

    pack = packet.get("pack") if isinstance(packet.get("pack"), dict) else {}
    for key in ("path", "state", "version_or_review_date"):
        if not nonempty(pack.get(key)):
            errors.append(f"task packet pack.{key} is empty")
    if nonempty(pack.get("path")) and not os.path.isfile(resolve(root, pack["path"])):
        errors.append(f"task packet pack path does not exist: {pack['path']}")

    shared = packet.get("shared_context") if isinstance(packet.get("shared_context"), dict) else {}
    for key in ("orientation_manifest", "state_interface"):
        if not nonempty(shared.get(key)):
            errors.append(f"task packet shared_context.{key} is empty")
        elif not os.path.isfile(resolve(root, shared[key])):
            errors.append(f"task packet shared_context.{key} does not exist: {shared[key]}")

    artifact = packet.get("artifact") if isinstance(packet.get("artifact"), dict) else {}
    for key in ("path", "version_or_fingerprint"):
        if not nonempty(artifact.get(key)):
            errors.append(f"task packet artifact.{key} is empty")
    if nonempty(artifact.get("path")) and not os.path.isfile(resolve(root, artifact["path"])):
        errors.append(f"task packet artifact path does not exist: {artifact['path']}")

    for key in ("source_hierarchy", "acceptance_criteria", "adjacent_or_human_boundaries"):
        value = packet.get(key)
        if not isinstance(value, list) or not value:
            errors.append(f"task packet {key} must be a non-empty list")
    for source in paths(packet.get("source_hierarchy", [])):
        source = str(source)
        if source.startswith(("http://", "https://")):
            continue
        if not os.path.isfile(resolve(root, source)):
            errors.append(f"task packet source does not exist: {source}")
    for key in ("approved_decisions", "known_conflicts", "evidence_limits", "unknowns"):
        if not isinstance(packet.get(key), list):
            errors.append(f"task packet {key} must be a list, even when empty")
    learning = packet.get("prior_mfc_learning")
    if not isinstance(learning, dict) or any(key not in learning for key in ("accepted", "narrowed", "rejected")):
        errors.append("task packet prior_mfc_learning must contain accepted, narrowed and rejected")
    elif any(not isinstance(learning[key], list) for key in ("accepted", "narrowed", "rejected")):
        errors.append("task packet prior_mfc_learning values must be lists")
    return errors, packet


def validate_review_output(review_path, packet_path_value, specialist_id, mode, packet):
    errors = []
    text = open(review_path, encoding="utf-8").read()
    frontmatter = review_frontmatter(text)
    missing = sorted(REQUIRED_REVIEW_FRONTMATTER - set(frontmatter))
    if missing:
        errors.append(f"review missing frontmatter: {missing}")
    pack = packet.get("pack") if isinstance(packet.get("pack"), dict) else {}
    artifact = packet.get("artifact") if isinstance(packet.get("artifact"), dict) else {}
    expected = {
        "specialist_id": specialist_id,
        "execution_mode": mode,
        "task_packet": packet_path_value,
        "pack_version": str(pack.get("version_or_review_date", "")),
        "pack_state": str(pack.get("state", "")),
        "artifact_reviewed": str(artifact.get("path", "")),
    }
    for key, expected_value in expected.items():
        if frontmatter.get(key) != expected_value:
            errors.append(f"review {key} does not match the task packet/routing record")

    bodies = {}
    for index, heading in enumerate(REQUIRED_REVIEW_HEADINGS):
        body = section_body(text, heading, REQUIRED_REVIEW_HEADINGS[index + 1:])
        bodies[heading] = body
        if body is None:
            errors.append(f"review missing section: {heading}")
        elif len(body) < 12:
            errors.append(f"review section is empty or a stub: {heading}")
    source_body = bodies.get("Sources reviewed") or ""
    source_values = [str(item) for item in paths(packet.get("source_hierarchy", []))]
    if source_values and not any(source in source_body for source in source_values):
        errors.append("review Sources reviewed does not name any task-packet source")
    return errors


def validate_record(path, root=ROOT):
    data = yaml.safe_load(open(path, encoding="utf-8")) or {}
    data["_record_filename"] = os.path.basename(path)
    errors = []
    if data.get("schema_version") != 2:
        return ["new routing record must use schema_version: 2"]
    for key in ("objective", "task_session_id", "material_prompt_fingerprint", "material_task_id"):
        if not nonempty(data.get(key)):
            errors.append(f"material routing record missing {key}")
    errors.extend(validate_coverage_screen(data, root))
    errors.extend(validate_coverage_challenge(data))
    default_mode = data.get("execution_mode")
    default_learning = data.get("learning_disposition")
    claimed_outputs = {}
    specialists = data.get("specialists") or []
    if not specialists and not nonempty(data.get("no_specialist_execution_reason")):
        errors.append("routing record with no executed specialist requires no_specialist_execution_reason")
    for item in specialists:
        specialist_id = str(item.get("id", "missing-id"))
        mode = item.get("execution_mode", default_mode)
        learning = item.get("learning_disposition", default_learning)
        if mode not in MODES:
            errors.append(f"{specialist_id}: invalid or missing execution_mode")
            continue
        if learning not in LEARNING:
            errors.append(f"{specialist_id}: invalid or missing learning_disposition")
        output_paths = paths(item.get("outputs", {}))
        if not output_paths:
            errors.append(f"{specialist_id}: no output evidence path")
            continue
        for output in output_paths:
            if not os.path.isfile(resolve(root, output)):
                errors.append(f"{specialist_id}: output does not exist: {output}")
        if mode in CONTRACT_REVIEW_MODES:
            task_packet = item.get("task_packet")
            if not task_packet or not os.path.isfile(resolve(root, task_packet)):
                errors.append(f"{specialist_id}: contract review missing saved task_packet")
                continue
            packet_errors, packet = validate_task_packet(resolve(root, task_packet), specialist_id, mode, root)
            errors.extend(f"{specialist_id}: {error}" for error in packet_errors)
            outputs = item.get("outputs") if isinstance(item.get("outputs"), dict) else {}
            review_output = outputs.get("review")
            if not nonempty(review_output):
                errors.append(f"{specialist_id}: contract review requires outputs.review")
                continue
            if review_output in claimed_outputs:
                errors.append(f"{specialist_id}: contract review reuses output already claimed by {claimed_outputs[review_output]}")
            claimed_outputs[review_output] = specialist_id
            if os.path.isfile(resolve(root, review_output)):
                review_errors = validate_review_output(
                    resolve(root, review_output), task_packet, specialist_id, mode, packet)
                errors.extend(f"{specialist_id}: {error}" for error in review_errors)
        elif mode == "reuse_current_evidence" and not nonempty(item.get("applicability_reason")):
            errors.append(f"{specialist_id}: reused evidence missing applicability_reason")
    return errors


def self_test():
    with tempfile.TemporaryDirectory() as root:
        os.makedirs(os.path.join(root, "records"))
        for name in ("pack.md", "orientation.yml", "state.md", "artifact.md", "source.md"):
            open(os.path.join(root, name), "w", encoding="utf-8").write((name + " evidence\n") * 30)
        packet = {
            "schema_version": 1, "specialist_id": "A-10", "execution_mode": "bounded_specialist_review",
            "pack": {"path": "pack.md", "state": "baseline_pack", "version_or_review_date": "2026-08-13"},
            "shared_context": {"orientation_manifest": "orientation.yml", "state_interface": "state.md"},
            "objective": "Test the learning architecture", "audience": "Adult participants",
            "lifecycle_stage": "internal_candidate",
            "artifact": {"path": "artifact.md", "version_or_fingerprint": "fixture-v1"},
            "bounded_question": "Does this architecture support learning without avoidable burden?",
            "decision_or_interface_informed": "Workshop architecture decision",
            "source_hierarchy": ["source.md"], "approved_decisions": [], "known_conflicts": [],
            "evidence_limits": ["No participant evidence"], "unknowns": ["Live room performance"],
            "prior_mfc_learning": {"accepted": [], "narrowed": [], "rejected": []},
            "acceptance_criteria": ["Identify a justified recommendation and strongest objection"],
            "adjacent_or_human_boundaries": ["Participant evidence remains external"],
        }
        packet_path = os.path.join(root, "packet.yml")
        yaml.safe_dump(packet, open(packet_path, "w", encoding="utf-8"), sort_keys=False)
        sections = []
        for heading in REQUIRED_REVIEW_HEADINGS:
            body = "source.md reviewed directly with a substantive finding and explicit limitation."
            sections.append(f"## {heading}\n\n{body}\n")
        review = ("---\nspecialist_id: A-10\nexecution_mode: bounded_specialist_review\n"
                  "pack_version: 2026-08-13\npack_state: baseline_pack\n"
                  "task_packet: packet.yml\nartifact_reviewed: artifact.md\n---\n\n"
                  "# Review\n\n" + "\n".join(sections))
        review_path = os.path.join(root, "review.md")
        open(review_path, "w", encoding="utf-8").write(review)
        record = {
            "schema_version": 2, "objective": "fixture objective", "task_session_id": "fixture-session",
            "material_prompt_fingerprint": "fixture-fingerprint",
            "material_task_id": "fixture-task",
            "bench_relevance_screen": [{"id": "A-10", "disposition": "route_now",
                                         "reason": "Learning architecture is decision-bearing."}],
            "coverage_challenge": {
                "selector": "A-04", "selector_context": "selector-fixture",
                "challenger": "A-24", "challenger_context": "challenger-fixture",
                "completed_before_execution": True,
                "decision_surfaces": ["learning architecture"],
                "omissions_challenged": ["A-11 omitted because this fixture has no measurement decision"],
                "changes": [], "unresolved": [], "reconciler": "SYS-04",
                "reconciliation": "Coverage retained with the recorded reason.",
            },
            "learning_disposition": "candidate_update",
            "specialists": [{"id": "A-10", "execution_mode": "bounded_specialist_review",
                             "task_packet": "packet.yml", "outputs": {"review": "review.md"}}],
        }
        record_path = os.path.join(root, "record.yml")
        yaml.safe_dump(record, open(record_path, "w", encoding="utf-8"), sort_keys=False)
        assert not validate_record(record_path, root), validate_record(record_path, root)

        open(review_path, "w", encoding="utf-8").write(review.replace("## Sources reviewed", "## Sources omitted"))
        assert any("missing section: Sources reviewed" in error for error in validate_record(record_path, root))
        open(review_path, "w", encoding="utf-8").write(review)

        no_source_trace = review.replace(
            "## Sources reviewed\n\nsource.md reviewed directly with a substantive finding and explicit limitation.",
            "## Sources reviewed\n\nThe review used background material but does not identify it here.")
        open(review_path, "w", encoding="utf-8").write(no_source_trace)
        assert any("does not name any task-packet source" in error for error in validate_record(record_path, root))
        open(review_path, "w", encoding="utf-8").write(review)

        packet_bad = dict(packet)
        packet_bad["audience"] = None
        yaml.safe_dump(packet_bad, open(packet_path, "w", encoding="utf-8"), sort_keys=False)
        assert any("field is empty: audience" in error for error in validate_record(record_path, root))
        yaml.safe_dump(packet, open(packet_path, "w", encoding="utf-8"), sort_keys=False)

        record["specialists"].append({"id": "A-11", "execution_mode": "bounded_specialist_review",
                                      "task_packet": "packet.yml", "outputs": {"review": "review.md"},
                                      "learning_disposition": "no_new_learning"})
        yaml.safe_dump(record, open(record_path, "w", encoding="utf-8"), sort_keys=False)
        assert any("reuses output" in error for error in validate_record(record_path, root))

        restricted_packet = dict(packet)
        restricted_packet["specialist_id"] = "A-12"
        restricted_packet["execution_mode"] = "restricted_screen"
        yaml.safe_dump(restricted_packet, open(packet_path, "w", encoding="utf-8"), sort_keys=False)
        restricted_review = (review.replace("specialist_id: A-10", "specialist_id: A-12")
                                   .replace("execution_mode: bounded_specialist_review",
                                            "execution_mode: restricted_screen"))
        open(review_path, "w", encoding="utf-8").write(restricted_review)
        restricted_record = {
            "schema_version": 2, "objective": "fixture objective", "task_session_id": "fixture-session",
            "material_prompt_fingerprint": "fixture-fingerprint",
            "material_task_id": "fixture-task",
            "bench_relevance_screen": [{"id": "A-10", "disposition": "not_relevant",
                                         "reason": "Learning is outside this restricted fixture."},
                                        {"id": "A-12", "disposition": "human_boundary",
                                         "reason": "Qualified-human boundary remains."}],
            "coverage_challenge": {
                "selector": "A-04", "selector_context": "selector-fixture-2",
                "challenger": "A-24", "challenger_context": "challenger-fixture-2",
                "completed_before_execution": True,
                "decision_surfaces": ["restricted safety screen"],
                "omissions_challenged": ["H-01 remains external qualified-human authority"],
                "changes": [], "unresolved": ["human approval pending"], "reconciler": "SYS-04",
                "reconciliation": "Restricted AI screen retained; human gate remains.",
            },
            "learning_disposition": "no_new_learning",
            "specialists": [{"id": "A-12", "execution_mode": "restricted_screen",
                             "task_packet": "packet.yml", "outputs": {"review": "review.md"}}],
        }
        yaml.safe_dump(restricted_record, open(record_path, "w", encoding="utf-8"), sort_keys=False)
        assert not validate_record(record_path, root), validate_record(record_path, root)

        load_bench_ids.cache_clear()
        load_bench_ids(ROOT)
        misses_after_first_call = load_bench_ids.cache_info().misses
        load_bench_ids(ROOT)
        assert load_bench_ids.cache_info().misses == misses_after_first_call, (
            "load_bench_ids must be cached per root -- re-parsing the 2600+ line bench file on "
            "every routing record is what made a full-directory scan exceed the calling hook's "
            "timeout budget (L-074)")
        load_bench_ids.cache_clear()

        # --- Regression: the rubber-stamp screen (2026-09-02) ---------------------------
        # Built from the real defect, not an invented case. 58 of 59 routing records
        # carried ONE exclusion reason repeated across 20+ roles, because
        # make_routing_record.py stamped a single --not-relevant-reason across every
        # remaining role. Both halves are tested: the validator must catch a stamped
        # screen, must accept a genuinely reasoned one, and must leave pre-cutoff
        # records alone -- retro-failing 58 historical records would block all work.

        def screen_of(reasons, date):
            return ({"date": date},
                    [{"id": f"A-{i:02d}", "disposition": "not_relevant", "reason": r}
                     for i, r in enumerate(reasons, start=1)])

        stamped = ["No question in this role's domain arose in this task."] * 20
        data, screen = screen_of(stamped, "2026-09-02")
        assert validate_screen_is_reasoned(data, screen), (
            "a screen with 20 excluded roles sharing one reason must be rejected -- this is "
            "the exact shape of the 58 records measured on 2026-09-02")

        reasoned = [f"A-{i:02d} (domain {i}): no question in this domain arose." for i in range(1, 21)]
        data, screen = screen_of(reasoned, "2026-09-02")
        # filename-dated pre-cutoff record is grandfathered even with no date field
        assert not validate_screen_is_reasoned({"_record_filename": "2026-08-01-x.yml"}, screen), (
            "pre-cutoff record (filename date) must be grandfathered")
        assert not validate_screen_is_reasoned(data, screen), (
            "a screen whose reasons each name their own domain must pass")

        data, screen = screen_of(stamped, "2026-08-15")
        assert not validate_screen_is_reasoned(data, screen), (
            "records before the cutoff are grandfathered deliberately; failing them would "
            "block every task to repair nothing")

        mostly_stamped = ["one reason"] * 19 + ["a genuinely different reason"]
        data, screen = screen_of(mostly_stamped, "2026-09-02")
        assert validate_screen_is_reasoned(data, screen), (
            "one distinct reason among twenty does not make a screen reasoned")

        data, screen = screen_of(["a", "b", "c"], "2026-09-02")
        assert not validate_screen_is_reasoned(data, screen), (
            "below four exclusions there is no stamp pattern to detect")

    print("PASS: specialist call contract self-test (bounded + restricted positive cases; "
          "missing section, source trace, context and unique output negatives; "
          "rubber-stamp screen caught, reasoned screen accepted, pre-cutoff grandfathered)")
    return 0


def main():
    if "--self-test" in sys.argv:
        return self_test()

    # A single-record path argument validates just that record (the Stop hook's fast path).
    # Without one, validate the whole live corpus (the periodic comprehensive audit).
    single_path = next((arg for arg in sys.argv[1:] if not arg.startswith("--")), None)
    if single_path:
        filename = os.path.basename(single_path)
        if filename in LEGACY_RECORDS:
            print(f"PASS: {filename} is an allowlisted legacy record, skipped")
            return 0
        failures = [f"{filename}: {error}" for error in validate_record(single_path)]
        if failures:
            print("FAIL: specialist call contract routing record")
            for failure in failures:
                print(f"  - {failure}")
            return 1
        print(f"PASS: {filename} satisfies universal packet + output contract")
        return 0

    failures = []
    checked = 0
    for filename in sorted(os.listdir(ROUTING_DIR)):
        if not filename.endswith(".yml") or filename in LEGACY_RECORDS:
            continue
        checked += 1
        for error in validate_record(os.path.join(ROUTING_DIR, filename)):
            failures.append(f"{filename}: {error}")
    if failures:
        print("FAIL: specialist call contract routing records")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print(f"PASS: {checked} post-contract routing record(s) satisfy universal packet + output contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
