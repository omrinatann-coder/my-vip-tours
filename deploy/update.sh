#!/usr/bin/env bash
# Pull, build, check, and switch atomically. Run as root: sudo bash /opt/my-vip-tours/deploy/update.sh
# Cron runs it every 30 minutes (deploy/my-vip-tours.cron); it only rebuilds when
# GitHub has new commits, e.g. the weekly article. --force rebuilds anyway.
set -euo pipefail
APP=/opt/my-vip-tours
WEB=/var/www/my-vip-tours
cd "$APP"
OLD=$(git rev-parse HEAD)
git pull -q --ff-only
if [ "$(git rev-parse HEAD)" = "$OLD" ] && [ -e "$WEB/current" ] && [ "${1:-}" != "--force" ]; then exit 0; fi
python3 build.py
python3 tests/check.py          # stops here (site unchanged) if anything is broken
REL="$WEB/releases/$(date +%Y%m%d%H%M%S)"
mkdir -p "$REL"
cp -a dist/. "$REL/"
ln -sfn "$REL" "$WEB/current.tmp" && mv -T "$WEB/current.tmp" "$WEB/current"
nginx -t -q && systemctl reload nginx   # picks up the new redirects.map
ls -1dt "$WEB"/releases/* | tail -n +6 | xargs -r rm -rf   # keep 5 releases for rollback
echo "Live: $REL"
