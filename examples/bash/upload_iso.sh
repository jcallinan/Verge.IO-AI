#!/bin/bash
# usage: upload_iso.sh file.iso
set -euo pipefail
. "$(dirname "$0")/common.sh"
f=$1
key=$(api POST files -d "{\"name\":\"$(basename "$f")\",\"type\":\"iso\"}" | python3 -c 'import json,sys;print(json.load(sys.stdin)["$key"])')
curl "${CURL_OPTS[@]}" "${AUTH[@]}" -X PUT -H 'Content-Type: application/octet-stream' --data-binary @"$f" "https://$VERGE_HOST/v4/files/$key/upload"
