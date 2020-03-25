#!/bin/bash

TRAP_CONF="/home/pi/template.bash/trap.conf"

declare -i SLEEP=`cat $TRAP_CONF`

# Process repeat times; default is 100 times
declare TIMES=100
[ ! -z "$1" ] && [ `echo $1 | egrep '^[0-9]+$'` ] && TIMES=$1	# Check if $1 is an interger

# Create named pipe for communication
NPIPE=/tmp/pipe_trap.$$
if [ ! -p $NPIPE ]; then
	# echo "$NPIPE does NOT exist, creating....."
	mkfifo $NPIPE
	# mknod $NPIPE p				# Another way to create pipe
else
	echo "$NPIPE exist"
fi

# Bash trap list, could be find by `kill -l`
# 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
# 6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
# 11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
# 16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
# 21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ
# 26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR
# 31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
# 38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
# 43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
# 48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
# 53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
# 58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
# 63) SIGRTMAX-1  64) SIGRTMAX
# 
# A useful link: https://www.tutorialspoint.com/unix/unix-signals-traps.htm
trap "echo 'SIGHUP(01) received, run sub-routine'; READCONF" SIGHUP
trap "echo 'SIGINT(02, Ctrl-C) received, program exit'; rm $NPIPE; exit 1" SIGINT
trap "echo 'SIGQUIT(03) received.'" SIGQUIT
trap "echo 'SIGILL(04) received.'" SIGILL
trap "echo 'SIGTRAP(05) received.'" SIGTRAP
trap "echo 'SIGABRT(06) received.'" SIGABRT
trap "echo 'SIGBUS(07) received.'" SIGBUS
trap "echo 'SIGFPE(08) received.'" SIGFPE
trap "echo 'SIGKILL(09) received.'" SIGKILL
trap "echo 'SIGUSR1(10) received.'" SIGUSR1
trap "echo 'SIGSEGV(11) received.'" SIGSEGV
trap "echo 'SIGUSR2(12) received.'" SIGUSR2
trap "echo 'SIGPIPE(13) received.'" SIGPIPE
trap "echo 'SIGALRM(14) received.'" SIGALRM
trap "echo 'SIGTERM(15) received.'" SIGTERM
trap "echo 'SIGSTKFLT(16) received.'" SIGSTKFLT
trap "echo 'SIGCHLD(17) received.'" SIGCHLD
trap "echo 'SIGCONT(18) received.'" SIGCONT
trap "echo 'SIGSTOP(19) received.'" SIGSTOP
trap "echo 'SIGTSTP(20) received.'" SIGTSTP
trap "echo 'SIGTTIN(21) received.'" SIGTTIN
trap "echo 'SIGTTOU(22) received.'" SIGTTOU
trap "echo 'SIGURG(23) received.'" SIGURG
trap "echo 'SIGXCPU(24) received.'" SIGXCPU
trap "echo 'SIGXFSZ(25) received.'" SIGXFSZ
trap "echo 'SIGVTALRM(26) received.'" SIGVTALRM
trap "echo 'SIGPROF(27) received.'" SIGPROF
trap "echo 'SIGWINCH(28) received.'" SIGWINCH
trap "echo 'SIGIO(29) received.'" SIGIO
trap "echo 'SIGPWR(30) received.'" SIGPWR
trap "echo 'SIGSYS(31) received.'" SIGSYS
trap "echo 'Signal (32) received.'" 32		# No signal match number 32, process will be terminated with message "Unknown signal 32"
trap "echo 'Signal (33) received.'" 33		# No signal match number 33, process will be terminated with message "Unknown signal 33"
trap "echo 'SIGRTMIN(34) received.'" 34		# Use signal number is accepted.
trap "echo 'SIGRTMAC(64) received.'" 64		# Use signal number is accepted.

function READCONF() {
	echo "Re-read configuration file"
	[ -f $TRAP_CONF ] && SLEEP=`cat trap.conf`
	echo "New sleep timer is $SLEEP second(s)!"
}

while [ $TIMES -gt 0 ]; do
	if read -t 1 line <>$NPIPE; then			# Use <> to prevent hang in this step
		echo "Receive data from pipe, processing......"
		if [ $line ]; then
			if [[ "$line" == "quit" ]]; then
				echo "Receive command to exit."
				rm $NPIPE
				break
			else
				echo "Data $line received from pipe"
				declare line=''
			fi
		else
			echo "NO data received from pipe"
		fi
	fi
	echo -e "Now sleep for $SLEEP seconds, $TIMES times remained.\n"
	TIMES=$((TIMES -1))
	sleep $SLEEP
done

rm $NPIPE
