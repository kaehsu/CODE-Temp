#!/usr/bin/env bash
DIALOG="/usr/bin/dialog"
PROGNAME=$(echo $0 | awk -F/ '{print $NF}')
TEMPDIR="/dev/shm"

TMP_INPUT=${TEMPDIR}/${PROGNAME}-input.$$
TMP_OUTPUT=${TEMPDIR}/${PROGNAME}-output.$$
DEFAULTPWD="Dialogtest"
PROMPT="Enter your password:"

$DIALOG --insecure --passwordbox "$PROMPT" 10 40 2>$TMP_OUTPUT

INPUTPWD=$(cat $TMP_OUTPUT)
[ -n $INPUTPWD ] && echo "Input passwd is: $INPUTPWD"

[ -f $TMP_INPUT ] && rm $TMP_INPUT
[ -f $TMP_OUTPUT ] && rm $TMP_OUTPUT

[ -z $INPUTPWD ] && exit 1

exit 0
