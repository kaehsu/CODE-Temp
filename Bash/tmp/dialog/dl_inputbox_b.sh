#!/usr/bin/env bash
DIALOG="/usr/bin/dialog"

TMP="/tmp/$0.$$"
DEFAULTNAME="defaulthost.xinguard.com"
PROMPT="Please configure hostname:"

$DIALOG --inputbox "$PROMPT" 10 40 $DEFAULTNAME 2> $TMP

INPUTNAME=$(cat $TMP)
[ -z "$INPUTNAME" ] && INPUTNAME=$DEFAULTNAME
echo "Hostname is: $INPUTNAME"

[ -f $TMP ] && rm $TMP

exit 0