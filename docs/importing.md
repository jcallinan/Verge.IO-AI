# Importing to VergeOS

Supported inputs include VMDK, VHD/VHDX, QCOW2, RAW/IMG, ISO, OVA/OVF, and VergeOS VM exports.

## Methods
- **Files via API** – upload to the `files` table (`POST /v4/files` metadata, then upload the data to the returned upload endpoint; the UI Files page does the same). ISOs show up as media; disk images can be imported to a drive via `vm_drives`/`import` actions.
- **Import from URL / NAS** – VergeOS can pull from an HTTP(S) URL or an NAS-hosted volume (NFS/CIFS share): create the file/import record with the source URL.
- **VM export/import** – export a VM as a VergeOS-format file to a NAS volume; import on another system (cross-site moves, DR).
- **Site sync / replication** – use `cloud_snapshots` + sync between VergeOS systems for VM-level moves.
- **Tenants** – import into a tenant by authenticating to the tenant's API endpoint.

## Examples
- `examples/python/import_disk.py` – upload an image and create a VM using it.
- `examples/bash/upload_iso.sh` – upload an ISO.
- `examples/bash/convert_and_import.sh` – convert then import.

## Post import checklist
Firmware matches, disk interface (virtio-scsi/virtio), NIC model, guest agent/cloud-init, drivers, IP config.
