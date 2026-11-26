# Migrating from other platforms

| Source | Method |
|--------|--------|
| **Hyper-V** | Export VM, convert/import `.vhdx` (see importing.md); gen2 -> UEFI. Install VirtIO drivers; remove Hyper-V integration services. |
| **Proxmox / KVM / libvirt** | Copy `qcow2`/raw from storage; import directly; guests usually already have virtio. Match machine type/firmware (OVMF). |
| **Nutanix AHV** | Export disk images (Prism image service / acropolis `qcow2`) and import; or restore via backup. |
| **XCP-ng / XenServer** | Export XVA/VHD; convert with `qemu-img convert -O qcow2`; remove Xen tools, add virtio. |
| **AWS / Azure / GCP** | Export image (VM Import/Export to VMDK/VHD, managed disk SAS URL download, GCE image export), then import. |
| **Physical (P2V)** | Clonezilla/`dd` over SSH to a raw image, `disk2vhd` for Windows, or agent-based backup restore. |
| **OVA/OVF appliances** | Import directly (see importing.md). |
| **Backup products (Veeam, etc.)** | Restore/export as disk files, then import. |

General notes: convert with `qemu-img convert -p -O qcow2 src.vmdk dst.qcow2` when needed, always validate the checksum, and
run the smoke test after first boot. Script helper: `examples/bash/convert_and_import.sh`.
