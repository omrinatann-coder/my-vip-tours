#!/usr/bin/env bash
# Pull, build, check, and switch atomically. Run as root: sudo bash /opt/my-vip-tours/deploy/update.sh
set -euo pipefail
APP=/opt/my-vip-tours
WEB=/var/www/my-vip-tours
cd "$APP"
git pull --ff-only
python3 build.py
python3 tests/check.py          # stops here (site unchanged) if anything is broken
REL="$WEB/releases/$(date +%Y%m%d%H%M%S)"
mkdir -p "$REL"
cp -a dist/. "$REL/"
ln -sfn "$REL" "$WEB/current.tmp" && mv -T "$WEB/current.tmp" "$WEB/current"
nginx -t -q && systemctl reload nginx   # picks up the new redirects.map
ls -1dt "$WEB"/releases/* | tail -n +6 | xargs -r rm -rf   # keep 5 releases for rollback
echo "Live: $REL"
