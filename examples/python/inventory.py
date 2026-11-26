from verge_client import Verge

c = Verge()
for t in ("networks", "tenants", "users", "nodes", "clusters"):
    print("==", t)
    for r in c.get(t, fields="most"):
        print("  ", r.get("$key"), r.get("name"))
