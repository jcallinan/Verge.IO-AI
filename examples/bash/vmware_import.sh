#!/bin/bash
# usage: vmware_import.sh <service-name> <vm-name>  (field names vary per release; verify)
set -euo pipefail
. "$(dirname "$0")/common.sh"
svc=$(api GET "vmware_containers?filter=name%20eq%20'$1'" | python3 -c 'import json,sys;print(json.load(sys.stdin)[0]["$key"])')
api POST vm_imports -d "{\"container\":$svc,\"name\":\"import-$2\",\"vm_name\":\"$2\"}"
