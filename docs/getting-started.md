# Getting started with the VergeOS API

## Authentication
- **Basic auth**: `curl -k -u admin:pass https://HOST/v4/vms`
- **Session token**: `POST /sys/tokens` with `{"login":"admin","password":"..."}` returns `{"$key": "<token>"}`; send it as
  `x-yottabyte-token: <token>` on later calls. Delete it with `DELETE /sys/tokens/<key>` when done.
- Prefer a dedicated API user with the least privileges needed, and use valid TLS certificates (avoid `-k`/`verify=False` in production).

## Conventions
- Resources are tables: `/v4/vms`, `/v4/machines`, `/v4/networks`, `/v4/tenants`, `/v4/users`, `/v4/nodes`, `/v4/clusters`,
  `/v4/machine_snapshots`, `/v4/cloud_snapshots`, `/v4/vm_actions`, `/v4/tasks` ...
- `GET /v4/vms?filter=name eq 'web01'&fields=most` filters and selects fields (`fields=all|most|dashboard|name,key`).
- `POST` creates, `PUT /v4/vms/<key>` replaces/updates, `DELETE /v4/vms/<key>` removes.
- Actions are POSTs to an action table, e.g. `POST /v4/vm_actions` `{"vm": <key>, "action": "poweron"}`
  (`poweroff`, `kill`, `reset`, `snapshot`, `clone`...). Long-running work returns a task you can poll in `/v4/tasks`.
- Use a retry/timeout policy; poll for state (`machine.status`) rather than sleeping.

See `examples/python/verge_client.py` for a small reusable client.
