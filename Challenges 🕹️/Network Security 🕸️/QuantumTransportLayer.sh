#!/bin/sh 

IP_ADDRESS="5.75.221.48"
HOSTNAME="fl4gg.quantum-transport-layer.test"

if ! grep -q "$HOSTNAME" /etc/hosts; then
    # Add the entry to /etc/hosts
    echo "$IP_ADDRESS $HOSTNAME" | sudo tee -a /etc/hosts > /dev/null
    echo "Added $HOSTNAME to /etc/hosts."
fi

echo "$(gnutls-cli fl4gg.quantum-transport-layer.test:10503 --insecure --alpn=flag)"

if grep -q "$HOSTNAME" /etc/hosts; then
  # Remove the line containing the hostname
  sudo sed -i "/$HOSTNAME/d" /etc/hosts
  echo "Removed $HOSTNAME from /etc/hosts."
fi
