#!/usr/bin/env bash

DIALOG="/usr/bin/dialog"

$DIALOG --backtitle "Back title" \
        --title "MSGBOX title" \
        --msgbox "This is a test." 20 60

case $? in
  0)
     echo "Enter-key is pressed"
     ;;
  255)
     echo "ESC-key is pressed"
     ;;
  *)
     echo "Unknown condition; Ctrl-C?"
     ;;
esac
