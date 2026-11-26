"""Pre-flight for system updates: verify health, then list available update info. Applying is left to the UI/API after review."""
import subprocess
import sys

rc = subprocess.call([sys.executable, "health_report.py"])
if rc:
    sys.exit("Cluster not healthy; do not update")
from verge_client import Verge

c = Verge()
for t in ("update_settings", "update_packages"):
    try:
        print(t, c.get(t))
    except Exception as e:  # table names vary per release
        print(t, "unavailable:", e)
