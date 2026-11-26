# Administration automation recipes

| Task | Script |
|------|--------|
| List/filter VMs, health overview | `examples/python/list_vms.py` |
| Power actions (on/off/reset) | `examples/python/vm_power.py` |
| Snapshot before change, prune old | `examples/python/snapshots.py` |
| Clone / deploy from template | `examples/python/clone_vm.py` |
| Networks, tenants, users | `examples/python/inventory.py` |
| Nodes, alarms, capacity report | `examples/python/health_report.py` |
| Rolling updates of nodes (check, snapshot, apply, verify) | `examples/python/update_check.py` |
| Smoke / post-migration testing | `examples/python/smoke_test.py` |
| Backup to curl | `examples/bash/` |

## Practices
- Take a system/VM snapshot before any change; keep a rollback plan.
- Run scripts in CI against a lab VergeOS; schedule with cron/systemd timers or CI.
- Use per-script API users; store secrets in a vault, rotate tokens.
- Log task IDs and poll `/v4/tasks` for completion.
- Updates: check update status via the `update_*` tables / UI, ensure the cluster is healthy and N+1 capacity, update one node at a time (VergeOS performs rolling updates), verify with `health_report.py`.
- DR testing: restore a `cloud_snapshot` to an isolated network, run `smoke_test.py`, destroy.
- AI assistants (e.g., Copilot) can generate/review scripts; always review before running against production.
