#!/bin/bash
grim -g "$(slurp -b '#000000aa' -c '#ffffff' -w 1)" - | wl-copy
