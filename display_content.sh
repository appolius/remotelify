#!/bin/bash

CONTENT_DIR="$HOME/RemotelifyContent"
LOGFILE="$HOME/remotelify_display.log"

mkdir -p "$CONTENT_DIR"

echo "[$(date)] Starting VLC fullscreen playlist..." >> "$LOGFILE"

# Collect all .mp4 files into one VLC playlist command
PLAYLIST=()
for f in "$CONTENT_DIR"/*.mp4; do
  [ -f "$f" ] && PLAYLIST+=("$f")
done

# Exit if no video files found
if [ ${#PLAYLIST[@]} -eq 0 ]; then
  echo "[$(date)] No video files found in $CONTENT_DIR" >> "$LOGFILE"
  exit 1
fi

# Run a single VLC instance with the whole playlist
cvlc --fullscreen --no-osd --loop "${PLAYLIST[@]}" >> "$LOGFILE" 2>&1
