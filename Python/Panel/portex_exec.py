#!/usr/bin/env python3

import yaml
import subprocess
import argparse

with open('portex_run.yaml', 'r') as configFILE:
    CONFIG = configFILE.read()
runCONFIG = yaml.safe_load(CONFIG)


def execPROG(btnX, time):
    pressBTN = btnX
    pressTIME = time
    if pressBTN not in ('btnA', 'btnB', 'btnP'):
        print("Check button name: button name should be btnP, btnA or btnB")
        exit(1)
    if runCONFIG['btnPeriod']['prdA'] < pressTIME and pressTIME <= runCONFIG['btnPeriod']['prdB']:
        # print("Button {} exec {}".format(pressBTN, runCONFIG[pressBTN + '_A']['run']))
        processRET = subprocess.call(
            runCONFIG[pressBTN + '_A']['run'], shell=True)
    elif runCONFIG['btnPeriod']['prdB'] < pressTIME and pressTIME <= runCONFIG['btnPeriod']['prdC']:
        # print("Button {} exec {}".format(pressBTN, runCONFIG[pressBTN + '_B']['run']))
        processRET = subprocess.call(
            runCONFIG[pressBTN + '_B']['run'], shell=True)
    elif runCONFIG['btnPeriod']['prdC'] < pressTIME and pressTIME <= runCONFIG['btnPeriod']['prdD']:
        # print("Button {} exec {}".format(pressBTN, runCONFIG[pressBTN + '_C']['run']))
        processRET = subprocess.call(
            runCONFIG[pressBTN + '_C']['run'], shell=True)
    elif runCONFIG['btnPeriod']['prdD'] < pressTIME:
        # print("Button {} exec {}".format(pressBTN, runCONFIG[pressBTN + '_D']['run']))
        processRET = subprocess.call(
            runCONFIG[pressBTN + '_D']['run'], shell=True)
    else:
        print('No matched button name.')


def main():
    #
    # Command line argument
    parser = argparse.ArgumentParser(
        description='PORTEX Panel Program to execute pre-defined program')
    parser.add_argument('-b', '--button', type=str, help='Pressed button')
    parser.add_argument('-p', '--period', type=str, help='Press period')
    cargs = parser.parse_args()
    pressButton = cargs.button
    pressPeriod = cargs.period
    execPROG(pressButton, float(pressPeriod))


if __name__ == "__main__":
    main()
