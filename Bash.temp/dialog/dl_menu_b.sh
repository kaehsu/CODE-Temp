#!/usr/bin/env bash
DIALOG="/usr/bin/dialog"
CHOICETMP="/tmp/radiolist.$$"
MENUPROMPT="Please select your prefered FS type:"
OPTNUM=3

# example: use array to manage selection options
MENULIST=("ext2" "Use FS EXT2" "ext3" "Use FS EXT3" "ext4" "Use FS EXT4")
$DIALOG --help-button \
        --help-label "NEWHELP" \
        --menu "$MENUPROMPT" 30 60 $OPTNUM \
            "${MENULIST[0]}" "${MENULIST[1]}" \
            "${MENULIST[2]}" "${MENULIST[3]}" \
            "${MENULIST[4]}" "${MENULIST[5]}" 2>$CHOICETMP

FSTYPE=$(cat $CHOICETMP)
if [ -z $FSTYPE ]; then
  echo "You did not select anythong"
  exit 1
else
  echo "Your selection: $FSTYPE"
fi

[ -f $CHOICETMP ] && rm $CHOICETMP
exit 0