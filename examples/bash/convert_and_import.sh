#!/bin/bash
# usage: convert_and_import.sh <source-disk (vmdk|vhdx|vdi|raw)> <vm-name>
set -euo pipefail
src=$1; name=$2
qemu-img info "$src"
qemu-img convert -p -O qcow2 "$src" "/tmp/$name.qcow2"
sha256sum "/tmp/$name.qcow2"
python3 "$(dirname "$0")/../python/import_disk.py" "/tmp/$name.qcow2" "$name"
