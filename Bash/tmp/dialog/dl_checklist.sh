#!/usr/bin/env bash
DIALOG="/usr/bin/dialog"
PROGNAME=$(echo $0 | awk -F/ '{print $NF}')
TEMPDIR="/dev/shm"
TMP_INPUT=${TEMPDIR}/${PROGNAME}-input.$$
TMP_OUTPUT=${TEMPDIR}/${PROGNAME}-output.$$

CHECKLISTPROMPT="Please select your prefered FS type:"
OPTNUM=3

CHECKLIST=("ext2" "Use FS EXT2" "ext3" "Use FS EXT3" "ext4" "Use FS EXT4")
$DIALOG --checklist "$CHECKLISTPROMPT" 10 40 $OPTNUM \
            "${CHECKLIST[0]}" "${CHECKLIST[1]}" OFF \
            "${CHECKLIST[2]}" "${CHECKLIST[3]}" ON \
            "${CHECKLIST[4]}" "${CHECKLIST[5]}" OFF 2>$TMP_OUTPUT

FSTYPE=$(cat $TMP_OUTPUT)
echo $FSTYPE

[ -f $TMP_INPUT ] && rm $TMP_INPUT
[ -f $TMP_OUTPUT ] && rm $TMP_OUTPUT

if [ -z "$FSTYPE" ]; then
  echo "Your selection: ${CHECKLIST[2]} by default"
  exit 1
else
  echo "Your selection: $FSTYPE"
  exit 0
fi

# It's a comment


