#!/usr/bin/env bash
# First install on the server (34.46.194.89), next to TaxiApp. Run as root:
#   sudo bash install.sh https://github.com/<owner>/my-vip-tours.git
# Safe before the DNS switch: nginx serves the site for my-vip-tours.com, but
# visitors still reach Base44 until the A records at IONOS point here.
set -euo pipefail
REPO=${1:?usage: install.sh <git url>}
APP=/opt/my-vip-tours
if [ ! -d "$APP/.git" ]; then git clone "$REPO" "$APP"; fi
bash "$APP/deploy/update.sh"
install -m 644 "$APP/deploy/nginx-my-vip-tours.conf" /etc/nginx/sites-available/my-vip-tours
# "zz-" makes nginx load this site after TaxiApp's, so TaxiApp stays the default
# site for requests that name no known domain (e.g. by IP address).
ln -sf /etc/nginx/sites-available/my-vip-tours /etc/nginx/sites-enabled/zz-my-vip-tours
nginx -t && systemctl reload nginx
install -m 644 "$APP/deploy/my-vip-tours.cron" /etc/cron.d/my-vip-tours
echo "Installed. Test before DNS:  curl -sI -H 'Host: my-vip-tours.com' http://127.0.0.1/ben-gurion-airport-transfers"
echo "After the DNS switch:       sudo bash $APP/deploy/https.sh you@example.com"
