#!/usr/bin/env python3

import yaml
import subprocess
import argparse
from datetime import datetime

with open('portex_cmd.yaml', 'r') as configFILE:
    CONFIG = configFILE.read()
runCONFIG = yaml.safe_load(CONFIG)


def execCMD(btnX, time):
    pressBTN = btnX
    pressTIME = time
    cmdSTART = datetime.today().strftime('%Y-%b-%d %H:%M:%S.%f')[:-3]
    if pressBTN not in ('btnA', 'btnB', 'btnP'):
        print("Check button name: button name should be btnP, btnA or btnB")
        exit(1)
    if runCONFIG['btnPeriod']['prdA'] < pressTIME and pressTIME <= runCONFIG['btnPeriod']['prdB']:
        # print("Button {} exec {}".format(pressBTN, runCONFIG[pressBTN + '_A']['cmd']))
        runCMD = runCONFIG[pressBTN + '_A']['cmd']
        pRET = subprocess.call(runCMD, shell=True)
    elif runCONFIG['btnPeriod']['prdB'] < pressTIME and pressTIME <= runCONFIG['btnPeriod']['prdC']:
        # print("Button {} exec {}".format(pressBTN, runCONFIG[pressBTN + '_B']['cmd']))
        runCMD = runCONFIG[pressBTN + '_B']['cmd']
        pRET = subprocess.call(runCMD, shell=True)
    elif runCONFIG['btnPeriod']['prdC'] < pressTIME and pressTIME <= runCONFIG['btnPeriod']['prdD']:
        # print("Button {} exec {}".format(pressBTN, runCONFIG[pressBTN + '_C']['cmd']))
        runCMD = runCONFIG[pressBTN + '_C']['cmd']
        pRET = subprocess.call(runCMD, shell=True)
    elif runCONFIG['btnPeriod']['prdD'] < pressTIME:
        # print("Button {} exec {}".format(pressBTN, runCONFIG[pressBTN + '_D']['cmd']))
        runCMD = runCONFIG[pressBTN + '_D']['cmd']
        pRET = subprocess.call(runCMD, shell=True)
    else:
        print('No matched button name.')
    cmdEND = datetime.today().strftime('%Y-%b-%d %H:%M:%S.%f')[:-3]
    with open('/tmp/portex_exec.log', 'at') as execLOG:
        execLOG.write(cmdSTART + "\n" + runCMD + "\n" + cmdEND + "\n\n")


def main():
    #
    # Command line argument
    parser = argparse.ArgumentParser(
        description='PORTEX Panel Program to execute pre-defined command.')
    parser.add_argument('-b', '--button', type=str,
                        help='Pressed button', required=True)
    parser.add_argument('-p', '--period', type=str,
                        help='Press period', required=True)
    cargs = parser.parse_args()
    pressButton = cargs.button
    pressPeriod = cargs.period
    execCMD(pressButton, float(pressPeriod))


if __name__ == "__main__":
    main()
