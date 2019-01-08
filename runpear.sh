#!/bin/bash

echo "waiting for usb sound devices to initialize"
python3 /home/pi/pear/wait_devices_init.py

echo "waiting sound devices have initialized, running pear"
python3 /home/pi/pear/pear.py /mnt/usb
