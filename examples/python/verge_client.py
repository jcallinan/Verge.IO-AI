"""Minimal VergeOS v4 API client. Credentials come from environment variables."""
import os
import time
import requests


class Verge:
    def __init__(self, host=None, user=None, password=None, token=None, verify=True):
        self.base = "https://%s/v4" % (host or os.environ["VERGE_HOST"])
        self.s = requests.Session()
        self.s.verify = verify and os.environ.get("VERGE_INSECURE") != "1"
        token = token or os.environ.get("VERGE_TOKEN")
        if token:
            self.s.headers["x-yottabyte-token"] = token
        else:
            self.s.auth = (user or os.environ["VERGE_USER"], password or os.environ["VERGE_PASS"])
        self.s.headers["Content-Type"] = "application/json"

    def _req(self, method, path, **kw):
        r = self.s.request(method, "%s/%s" % (self.base, path.lstrip("/")), timeout=60, **kw)
        r.raise_for_status()
        return r.json() if r.content else None

    def get(self, path, **params):
        return self._req("GET", path, params=params)

    def post(self, path, body):
        return self._req("POST", path, json=body)

    def put(self, path, body):
        return self._req("PUT", path, json=body)

    def delete(self, path):
        return self._req("DELETE", path)

    def vms(self, **params):
        return self.get("vms", **params)

    def vm_action(self, vm_key, action, **extra):
        return self.post("vm_actions", dict({"vm": vm_key, "action": action}, **extra))

    def find_vm(self, name):
        res = self.get("vms", filter="name eq '%s'" % name.replace("'", ""), fields="most")
        return res[0] if res else None

    def wait(self, fn, timeout=600, interval=5):
        end = time.time() + timeout
        while time.time() < end:
            v = fn()
            if v:
                return v
            time.sleep(interval)
        raise TimeoutError("condition not met in %ss" % timeout)
