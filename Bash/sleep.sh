#!/bin/bash

trap "echo 'Receive trap SIGHUP(1)'" SIGHUP
trap "echo 'Receive trap SIGCHLD(17)'" SIGCHLD
TIMES=100

while [ $TIMES -gt 0 ]; do
  echo "There are $TIMES remained."
  TIMES=$((TIMES - 1))
  sleep 1
done

