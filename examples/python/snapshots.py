"""Snapshot a VM: snapshots.py <vm-name> [--prune-days N]. Field names vary by release; verify."""
import sys
import time
from verge_client import Verge

c = Verge()
vm = c.find_vm(sys.argv[1])
if not vm:
    sys.exit("VM not found")
name = "auto-%s" % time.strftime("%Y%m%d-%H%M%S")
print(c.vm_action(vm["$key"], "snapshot", params={"name": name}))
if "--prune-days" in sys.argv:
    days = int(sys.argv[sys.argv.index("--prune-days") + 1])
    cutoff = time.time() - days * 86400
    for s in c.get("machine_snapshots", filter="machine eq %s" % vm["machine"]):
        if s.get("name", "").startswith("auto-") and s.get("created", 0) < cutoff:
            c.delete("machine_snapshots/%s" % s["$key"])
            print("pruned", s["name"])
