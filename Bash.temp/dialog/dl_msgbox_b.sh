#!/usr/bin/env bash
DIALOG="/usr/bin/dialog"

$DIALOG --msgbox "Dialog msgbox test" 10 40

if [ $? -eq 0 ]; then
  echo 'Enter key detected'
elif [ $? -eq 255 ]; then
  echo 'ESC key detected'
else
  echo 'Ctrl-C detected'
fi

exit 0
