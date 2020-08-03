#!/usr/bin/env bash
DIALOG="/usr/bin/dialog"
PROGNAME=$(echo $0 | awk -F/ '{print $NF}')
TEMPDIR="/dev/shm"

{
	for ((i = 1; i <= 10; i++)); do
		let I=10*i
		echo $I
		sleep 1
	done
	echo
	for ((i = 9; i >= 0; i--)); do
		let I=10*i
		echo $I
		sleep 1
	done
} | $DIALOG --guage "Installation procedure....." 10 40 0
