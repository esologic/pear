# PEAR - a simple tool for sound installations.

Take a directory with `.wav` files named in numeric order
and play them over usb sound devices attached to the host computer.

Right now, the project only supports debian-based Linux, and the USB-AUDIO from Plugable, which is based on the C-Media HS 100B. It would be very easy to support more devices, make an issue or just send a PR.

## Prerequisites

This project is based on the [sounddevice](https://github.com/spatialaudio/python-sounddevice/) python package, which can be tricky to install.

Run the following command to install the prerequisite debian packages:

```
 sudo apt-get install python3-pip python3-numpy libportaudio2 libsndfile1
```

Then install pyaudio

```
python3 -m pip install sounddevice soundfile
```

## Run Manually

Run `pear.py` with the command line argument of the folder the sound files are kept in.

All sound files will start playing at the same time, and will restart once the longest one has finished playing.

Example:

```
$ python3 pear.py ./test
```


## Auto Mounting USB Drive

In a typically art installation use case, you don't want to have to plug in a keyboard and monitor in order to change the audio file.

You can use a USB drive

```
sudo mkdir /mnt/usb/
```

Edit your `/etc/fstab`, adding the following line:
```
LABEL=PEAR /mnt/usb vfat defaults,auto,umask=000,users,ro,nofail 0 0
```

## Run at Boot