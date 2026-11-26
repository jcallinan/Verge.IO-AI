# source this: requires VERGE_HOST and (VERGE_TOKEN or VERGE_USER/VERGE_PASS)
: "${VERGE_HOST:?set VERGE_HOST}"
if [ -n "$VERGE_TOKEN" ]; then AUTH=(-H "x-yottabyte-token: $VERGE_TOKEN"); else AUTH=(-u "${VERGE_USER:?}:${VERGE_PASS:?}"); fi
CURL_OPTS=(-sS --fail-with-body)
[ "$VERGE_INSECURE" = 1 ] && CURL_OPTS+=(-k)
api() { local m=$1 p=$2; shift 2; curl "${CURL_OPTS[@]}" "${AUTH[@]}" -X "$m" -H 'Content-Type: application/json' "https://$VERGE_HOST/v4/$p" "$@"; }
