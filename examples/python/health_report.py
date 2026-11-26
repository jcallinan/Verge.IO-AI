"""Capacity and health overview; exits non-zero when nodes are not online or alarms exist."""
import sys
from verge_client import Verge

c = Verge()
bad = 0
for n in c.get("nodes", fields="most"):
    st = n.get("status", n.get("machine_status", "unknown"))
    print("node", n.get("name"), st)
    bad += st not in ("running", "online")
alarms = c.get("alarms", fields="most")
for a in alarms:
    print("alarm", a.get("level"), a.get("description", a.get("alarm_id")))
sys.exit(1 if bad or alarms else 0)
