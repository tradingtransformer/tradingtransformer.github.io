#!/usr/bin/env bash
# Push every URL in sitemap.xml to IndexNow (instantly notifies Bing, Yandex, etc.).
# Run after each deploy:  ./indexnow-submit.sh
set -euo pipefail

HOST="www.tradingtransformer.com"
KEY="89cbebd9dc814ded8ba7e82926a405bf"
KEY_LOCATION="https://${HOST}/${KEY}.txt"

cd "$(dirname "$0")"

# Pull <loc> URLs out of the sitemap.
URLS=$(grep -oE '<loc>[^<]+</loc>' sitemap.xml | sed -E 's#</?loc>##g')

# Build the JSON urlList array.
URL_JSON=$(printf '%s\n' "$URLS" | sed 's/.*/"&"/' | paste -sd, -)

PAYLOAD=$(cat <<JSON
{"host":"${HOST}","key":"${KEY}","keyLocation":"${KEY_LOCATION}","urlList":[${URL_JSON}]}
JSON
)

echo "Submitting $(printf '%s\n' "$URLS" | grep -c . ) URLs to IndexNow…"
HTTP=$(curl -sS -o /tmp/indexnow_resp -w '%{http_code}' \
  -X POST 'https://api.indexnow.org/indexnow' \
  -H 'Content-Type: application/json; charset=utf-8' \
  --data-raw "$PAYLOAD")

echo "HTTP $HTTP"
cat /tmp/indexnow_resp 2>/dev/null || true
echo
# 200 = accepted, 202 = received/pending. Anything else is an error.
[[ "$HTTP" == "200" || "$HTTP" == "202" ]]
