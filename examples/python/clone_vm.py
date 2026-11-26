"""clone_vm.py <source-vm> <new-name>"""
import sys
from verge_client import Verge

c = Verge()
src = c.find_vm(sys.argv[1])
if not src:
    sys.exit("source not found")
print(c.vm_action(src["$key"], "clone", params={"name": sys.argv[2]}))
