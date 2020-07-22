#!/usr/bin/env bash
DIALOG="/usr/bin/dialog"
PROGNAME=$(echo $0 | awk -F/ '{print $NF}')
TEMPDIR="/dev/shm"

{
	for ((i = 1; i <= 100; i++)); do
		echo $((RANDOM % 100))
		sleep 0.01
	done
} | $DIALOG --guage "Installation progress" 10 40

exit 0
