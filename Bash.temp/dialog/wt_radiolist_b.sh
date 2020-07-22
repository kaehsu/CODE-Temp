#!/usr/bin/env bash
DIALOG="/bin/whiptail"
CHOICETMP="/tmp/radiolist.$$"
MENUPROMPT="Please select your prefered FS type:"
OPTNUM=3

# example: use string to manage selection optoins
#MENULIST='ext2 "Use_FS_ext2" off ext3 "USE_FS_ext3" on ext4 "USE_FS_ext4" off'
#$DIALOG --radiolist "$MENUPROMPT" 30 60 $OPTNUM $MENULIST 2> $CHOICETMP

# example: use array to manage selection options
MENULIST=("ext2" "Use FS EXT2" "ext3" "Use FS EXT3" "ext4" "Use FS EXT4")
$DIALOG --radiolist "$MENUPROMPT" 30 60 $OPTNUM \
  "${MENULIST[0]}" "${MENULIST[1]}" OFF \
  "${MENULIST[2]}" "${MENULIST[3]}" ON \
  "${MENULIST[4]}" "${MENULIST[5]}" OFF 2>$CHOICETMP

FSTYPE=$(cat $CHOICETMP)
if [ -z $FSTYPE ]; then
  echo "Your selection: ${MENULIST[2]} by default"
  exit 1
else
  echo "Your selection: $FSTYPE"
fi

[ -f $CHOICETMP ] && rm $CHOICETMP
exit 0
