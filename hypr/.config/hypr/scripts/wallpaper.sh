#!/bin/bash

DIR="$HOME/Pictures/wallpapers"

IMG=$(find "$DIR" -type f | wofi --dmenu)

[ -z "$IMG" ] && exit

awww img "$IMG" \
  --transition-type grow \
  --transition-duration 1
