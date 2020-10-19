#!/usr/bin/env bash

echo -e "yellow_off\c" | sudo nc -q 1 -U /var/run/uds_led
