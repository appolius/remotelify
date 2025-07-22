#!/bin/bash

TRIGGER_FILE="/tmp/trigger-reboot"

while true; do
  if [ -f "$TRIGGER_FILE" ]; then
    echo "Reboot triggered by container"
    rm "$TRIGGER_FILE"
    reboot
  fi
  sleep 1
done

# chmod +x ~/watch_reboot.sh
# ./watch_reboot.sh &

