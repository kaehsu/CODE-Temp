#!/usr/bin/env bash

SIGN=$1
SSPID=$2

declare -a BYPASS=(2 9 19 32 33)

while [ $SIGN -le 64 ]; do
  [[ ! " ${BYPASS[@]} " =~ " ${SIGN} " ]] && echo "Send signal $SIGN" && kill -$SIGN $SSPID
  SIGN=$((SIGN +1))
  sleep 1
done
