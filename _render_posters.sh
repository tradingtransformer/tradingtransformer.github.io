#!/usr/bin/env bash
# Rasterize the poster SVGs -> PNGs with crisp text.
#
# Why this exists: qlmanage softens SVG text (poor antialiasing + generic font
# substitution), so headlines came out fuzzy. Chrome headless renders the real
# font stack with clean AA. We render at 2x (--force-device-scale-factor=2),
# centre-crop to the target W:H, then downscale for supersampled, sharp edges.
#
# Target W:H comes from the filename (…-1242x2688-… / …-1080x1350-…). The SVG
# canvas may be square (art in a centred column -> centre-crop) or already the
# portrait target (centre-crop is a no-op). Same code path handles both.
#
# Usage:  ./_render_posters.sh [glob ...]      (default: all poster SVGs)
set -euo pipefail

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[ -x "$CHROME" ] || { echo "Chrome not found at: $CHROME" >&2; exit 1; }

globs=("$@")
[ ${#globs[@]} -eq 0 ] && globs=(noark-*-1242x2688-*.svg noark-*-1080x1350-*.svg)

n=0
for svg in "${globs[@]}"; do
  [ -f "$svg" ] || continue
  tgt=$(echo "$svg" | grep -oE '[0-9]+x[0-9]+' | head -1)
  tw=${tgt%x*}; th=${tgt#*x}
  read -r cw ch < <(head -1 "$svg" | grep -oE 'width="[0-9]+" height="[0-9]+"' \
                    | grep -oE '[0-9]+' | tr '\n' ' ')
  out="${svg%.svg}.png"
  "$CHROME" --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    --window-size="${cw},${ch}" --default-background-color=00000000 \
    --screenshot="$out" "file://$PWD/$svg" >/dev/null 2>&1
  sips -c $((th*2)) $((tw*2)) "$out" >/dev/null    # centre-crop to target ratio @2x
  sips -z "$th" "$tw" "$out" >/dev/null            # downscale to target
  echo "rendered $out (${tw}x${th})"
  n=$((n+1))
done
echo "$n posters rendered"
