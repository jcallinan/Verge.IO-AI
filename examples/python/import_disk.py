"""Import a disk image: import_disk.py <image-file> <vm-name>. Uploads to /files then creates a VM.
Endpoints/fields vary by release; verify with the API docs."""
import os
import sys
from verge_client import Verge

path, name = sys.argv[1], sys.argv[2]
c = Verge()
f = c.post("files", {"name": os.path.basename(path), "type": "import"})
key = f["$key"]
with open(path, "rb") as fh:
    r = c.s.put("%s/files/%s/upload" % (c.base, key), data=fh, headers={"Content-Type": "application/octet-stream"}, timeout=None)
    r.raise_for_status()
print(c.post("vms", {"name": name, "cpu_cores": 2, "ram": 4096, "os_family": "linux"}))
print("attach file", key, "as a drive via the UI or vm_drives; see docs/importing.md")
