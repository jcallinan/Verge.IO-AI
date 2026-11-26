"""Create VMware import jobs in VergeOS from a CSV (vm_name,target_network,tier).
Env: VERGE_*; requires a VMware service already configured in VergeOS.
Table/field names are release-dependent: verify with the API docs; use --dry-run first."""
import argparse
import csv
from verge_client import Verge

ap = argparse.ArgumentParser()
ap.add_argument("--csv", required=True)
ap.add_argument("--service", required=True, help="name of the VMware service/integration in VergeOS")
ap.add_argument("--dry-run", action="store_true")
a = ap.parse_args()
c = Verge()
svc = c.get("vmware_containers", filter="name eq '%s'" % a.service.replace("'", ""))
if not svc:
    raise SystemExit("VMware service not found")
for row in csv.DictReader(open(a.csv)):
    body = {"container": svc[0]["$key"], "name": "import-" + row["vm_name"], "vm_name": row["vm_name"],
            "preferred_tier": row.get("tier", "1"), "network": row.get("target_network", "")}
    print("create import", body)
    if not a.dry_run:
        print(c.post("vm_imports", body))
