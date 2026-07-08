# Evidence Bundle: `2f87c0c1-4c64-4ba0-bcf0-b7a86893a3c2`

- Timestamp: `2026-07-08T07:33:06.627345+00:00`
- Harness: `local-agentic-coding-lab`
- Capability: `coding.bugfix`
- Mode: `standalone`
- Data boundary: `local_repo_only`
- Repo: `/private/var/folders/t9/s4yz0sms73j1ycq5_hkp28hw0000gp/T/workshop-student-spike-mivrldcn`
- Input: failing_test=tests.test_grouping.GroupExpensesByMonthTests.test_month_boundary_crosses_in_target_timezone

## Execution

- Model roles used: coder, summariser
- Runtime lanes used: ollama
- Model load/evict events: load:devstral-small-2:24b, load:qwen2.5-coder:7b
- Tools used: apply_patch_ast_check, apply_patch_dry_run, blast_radius_score, run_tests_with_patch
- Commands run: make python-test
- Files read: none recorded
- Files changed: none
- Patch generated: `True`
- Tests run: `passed`
- Blast-radius risk score: 2.0
- Eval result: none

## Follow-up

- Teaching trace: none
- Learning signals: Successfully fixed bug in run 2f87c0c1-4c64-4ba0-bcf0-b7a86893a3c2 using model devstral-small-2:24b.
- Safety approvals: none required
- Risks: none recorded
- Next actions: none recorded
