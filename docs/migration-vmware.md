# Migrating from VMware to VergeOS

## Options
1. **Built-in VMware import (recommended)** – add vCenter/ESXi as a *VMware Service* (Integration) in VergeOS, then
   create *import jobs* that read the VM through the VMware API (VADP/NFC), convert disks and create the VM. Supports
   scheduled/incremental sync (CBT) followed by a short cutover. Everything is available through the API/UI under the VM Import
   (`vm_imports` / `vmware_*` tables - confirm names on your release).
2. **Disk-level import** – export VMDKs (or OVA/OVF) and import to VergeOS (see `importing.md`), then create a VM attached to the disk.
3. **NAS/NFS staging** – mount the VMware datastore export (NFS) or a VergeOS NAS volume as a source and import the VMDK from there.
4. **In-guest tools / backup restore** – restore from Veeam/other backup or use agent-based tools for physical/unsupported cases.

## Workflow
1. **Assess** – inventory with `examples/python/vmware_inventory.py` (pyvmomi) to find sizes, firmware (BIOS/UEFI), NIC count,
   snapshots (consolidate first), VMware Tools, RDMs/independent disks (not importable as-is).
2. **Prepare VergeOS** – create target networks matching VLANs/port groups, pick storage tier, create a VMware service
   with a read-only vCenter account.
3. **Pre-migration guest prep** – install the VirtIO drivers on Windows (or use VergeOS' driver injection), remove VMware Tools after
   cutover, check `fstab`/initramfs on Linux (virtio modules, device naming), note static IP configs.
4. **Import** – create the import job via API (`examples/bash/vmware_import.sh`, `examples/python/vmware_import.py`), run an initial sync
   while the source is running.
5. **Cutover** – shut down the source, run the final sync, power on in VergeOS, fix NIC/IP, validate.
6. **Validate** – `examples/python/smoke_test.py` (power state, guest agent, ping/port checks), keep the source powered off for a rollback window.
7. **Clean up** – remove import jobs, delete source after retention, uninstall VMware Tools.

## Batch migration
Drive waves from a CSV (`vm_name,target_network,tier,cutover_time`) with `examples/python/vmware_import.py --csv wave1.csv`.
Run test-boots first using a clone with the NIC attached to an isolated network.

## Troubleshooting
- Windows boot `INACCESSIBLE_BOOT_DEVICE`: VirtIO storage driver missing; temporarily use SATA/IDE interface for the disk.
- UEFI vs BIOS mismatch: set the VM's firmware to match the source.
- Slow import: check vCenter NFC limits, network path and source datastore load.
