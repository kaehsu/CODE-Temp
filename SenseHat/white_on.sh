#!/usr/bin/env bash

echo -e "white_on\c" | sudo nc -q 1 -U /var/run/uds_led
