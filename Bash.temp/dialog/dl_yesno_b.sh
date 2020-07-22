#!/usr/bin/env bash
DIALOG="/usr/bin/dialog"
CHOICE=''

dialog --backtitle "Back title" \
       --title "MSGBOX title" \
       --yesno "Do you want to continuse?" 20 60

if [ $? -ne 0 ]; then
  echo 'No select, default is NO'
  exit 1
fi

if [ -n "$CHOICE" ]; then
  echo 'Your choice: NO'
else
  echo 'Your choice: YES'
fi

exit 0