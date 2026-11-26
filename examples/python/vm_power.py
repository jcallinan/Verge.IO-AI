"""Usage: vm_power.py <vm-name> <poweron|poweroff|kill|reset>"""
import sys
from verge_client import Verge

c = Verge()
vm = c.find_vm(sys.argv[1])
if not vm:
    sys.exit("VM not found")
print(c.vm_action(vm["$key"], sys.argv[2]))
