#!/usr/bin/env bash
#
#

RAW_FILENAME="$0"
FILENAME="$(echo $0 | awk -F/ '{print $NF}')"

echo $RAW_FILENAME
echo $FILENAME
