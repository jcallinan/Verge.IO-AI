# Verge.IO-AI
Examples of using the VergeOS (Verge.IO) REST API for automation: migration, testing, updates, and day-to-day administration.

> The examples target the VergeOS v4 REST API (`https://<host>/v4/<table>`). Table and field names can differ between
> releases. Verify against the built-in API docs on your system (Swagger UI under the system's `/api` documentation page)
> and test in a lab first. Never commit credentials; scripts read them from environment variables.

## Layout
| Path | Contents |
|------|----------|
| `docs/getting-started.md` | Authentication, API conventions, filtering, actions |
| `docs/migration-vmware.md` | Migrating from VMware vSphere/ESXi (primary guide) |
| `docs/migration-other.md` | Hyper-V, Proxmox/KVM, Nutanix, Xen/XCP-ng, cloud, physical |
| `docs/importing.md` | Importing disks/VMs: OVA/OVF, VMDK, VHDX, QCOW2, RAW, ISO, VM export/import, NAS |
| `docs/automation-recipes.md` | VM lifecycle, snapshots, networks, tenants, updates, monitoring, testing, DR |
| `examples/python/` | Python client (`verge_client.py`) and runnable scripts |
| `examples/bash/` | curl-based scripts |

## Quick start
```bash
export VERGE_HOST=verge.example.com VERGE_USER=admin VERGE_PASS='...'   # or VERGE_TOKEN
pip install -r examples/python/requirements.txt
python examples/python/list_vms.py
python examples/python/smoke_test.py
```
