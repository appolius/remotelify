#!/bin/bash

# Folder containing video files
CONTENT_DIR="$HOME/RemotelifyContent"
LOGFILE="$HOME/remotelify_display.log"

mkdir -p "$CONTENT_DIR"

echo "[$(date)] Starting VLC fullscreen loop..." >> "$LOGFILE"

while true; do
  for f in "$CONTENT_DIR"/*.mp4; do
    [ -f "$f" ] || continue
    cvlc --fullscreen --no-osd --play-and-exit "$f" >> "$LOGFILE" 2>&1
  done
done
