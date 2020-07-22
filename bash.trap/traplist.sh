#!/usr/bin/env bash

trap "echo 'SIGHUP(01) received.'" SIGHUP
trap "echo 'SIGINT(02, Ctrl-C) received.'; exit 1" SIGINT
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
trap "echo 'Signal (32) received.'" 32
trap "echo 'Signal (33) received.'" 33
trap "echo 'SIGRTMIN(34) received.'" 34
trap "echo 'SIGRTMIN(35) received.'" 35
trap "echo 'SIGRTMIN(36) received.'" 36
trap "echo 'SIGRTMIN(37) received.'" 37
trap "echo 'SIGRTMIN(38) received.'" 38
trap "echo 'SIGRTMIN(39) received.'" 39
trap "echo 'SIGRTMIN(40) received.'" 40
trap "echo 'SIGRTMIN(41) received.'" 41
trap "echo 'SIGRTMIN(42) received.'" 42
trap "echo 'SIGRTMIN(43) received.'" 43
trap "echo 'SIGRTMIN(44) received.'" 44
trap "echo 'SIGRTMIN(45) received.'" 45
trap "echo 'SIGRTMIN(46) received.'" 46
trap "echo 'SIGRTMIN(47) received.'" 47
trap "echo 'SIGRTMIN(48) received.'" 48
trap "echo 'SIGRTMAX(49) received.'" 49
trap "echo 'SIGRTMAX(50) received.'" 50
trap "echo 'SIGRTMAX(51) received.'" 51
trap "echo 'SIGRTMAX(52) received.'" 52
trap "echo 'SIGRTMAX(53) received.'" 53
trap "echo 'SIGRTMAX(54) received.'" 54
trap "echo 'SIGRTMAX(55) received.'" 55
trap "echo 'SIGRTMAX(56) received.'" 56
trap "echo 'SIGRTMAX(57) received.'" 57
trap "echo 'SIGRTMAX(58) received.'" 58
trap "echo 'SIGRTMAX(59) received.'" 59
trap "echo 'SIGRTMAX(60) received.'" 60
trap "echo 'SIGRTMAX(61) received.'" 61
trap "echo 'SIGRTMAX(62) received.'" 62
trap "echo 'SIGRTMAX(63) received.'" 63
trap "echo 'SIGRTMAX(64) received.'" 64

TIMES=100

while [ $TIMES -gt 0 ]; do
	echo -e "Total $TIMES remained\n"
	TIMES=$((TIMES -1))
	sleep 1
done
