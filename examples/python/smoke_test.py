"""Post-migration/DR smoke test: smoke_test.py [vm-name ...] ; checks VM running and optional TCP ports (--port host:port)."""
import socket
import sys
from verge_client import Verge

args = sys.argv[1:]
ports = [a.split("=", 1)[1] for a in args if a.startswith("--port=")]
names = [a for a in args if not a.startswith("--")]
c = Verge()
fail = 0
for vm in (c.find_vm(n) for n in names) if names else c.vms(fields="most"):
    if not vm:
        fail += 1
        continue
    st = str(vm.get("machine_status", vm.get("status", ""))).lower()
    ok = "run" in st
    print("PASS" if ok else "FAIL", vm.get("name"), st)
    fail += not ok
for hp in ports:
    h, p = hp.rsplit(":", 1)
    try:
        socket.create_connection((h, int(p)), timeout=5).close()
        print("PASS", hp)
    except OSError as e:
        print("FAIL", hp, e)
        fail += 1
sys.exit(1 if fail else 0)
