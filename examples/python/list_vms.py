from verge_client import Verge

for vm in Verge().vms(fields="most"):
    print(vm.get("$key"), vm.get("name"), vm.get("cpu_cores"), vm.get("ram"), vm.get("machine_status", vm.get("status", "")))
