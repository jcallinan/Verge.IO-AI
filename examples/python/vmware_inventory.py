"""Inventory vCenter VMs for migration planning. Env: VC_HOST VC_USER VC_PASS. Outputs CSV."""
import csv
import os
import ssl
import sys
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

ctx = ssl.create_default_context()
if os.environ.get("VC_INSECURE") == "1":
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
si = SmartConnect(host=os.environ["VC_HOST"], user=os.environ["VC_USER"], pwd=os.environ["VC_PASS"], sslContext=ctx)
try:
    view = si.content.viewManager.CreateContainerView(si.content.rootFolder, [vim.VirtualMachine], True)
    w = csv.writer(sys.stdout)
    w.writerow(["name", "cpus", "mem_mb", "firmware", "power", "snapshots", "disks_gb", "networks", "guest"])
    for vm in view.view:
        c = vm.config
        if not c:
            continue
        disks = [d.capacityInKB // 1048576 for d in c.hardware.device if isinstance(d, vim.vm.device.VirtualDisk)]
        nets = [n.name for n in vm.network]
        w.writerow([c.name, c.hardware.numCPU, c.hardware.memoryMB, c.firmware, vm.runtime.powerState,
                    bool(vm.snapshot), "+".join(map(str, disks)), "+".join(nets), c.guestFullName])
finally:
    Disconnect(si)
