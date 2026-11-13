#!/usr/bin/env bash
# After the IONOS A records point to this server: certificate + HTTPS redirect.
#   sudo bash /opt/my-vip-tours/deploy/https.sh you@example.com
set -euo pipefail
EMAIL=${1:?usage: https.sh <email for certificate notices>}
IP=$(curl -fsS -H "Metadata-Flavor: Google" \
  "http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/0/access-configs/0/external-ip" 2>/dev/null \
  || curl -fsS https://api.ipify.org)
for name in my-vip-tours.com www.my-vip-tours.com; do
  got=$(getent ahostsv4 "$name" | awk 'NR==1{print $1}')
  [ "$got" = "$IP" ] || { echo "DNS for $name points to '${got:-nothing}', expected $IP. Wait for the IONOS change to spread."; exit 1; }
done
certbot --nginx -d my-vip-tours.com -d www.my-vip-tours.com --non-interactive --agree-tos -m "$EMAIL" --redirect
nginx -t && systemctl reload nginx
curl -fsSI https://my-vip-tours.com/ben-gurion-airport-transfers | head -1
