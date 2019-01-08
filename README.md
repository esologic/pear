# PEAR - a tool for sound installations

Take a directory with `.wav` files named in numeric order
and play them over usb sound devices attached to the host computer over and over forever, looping all files once the longest one finishes.

`1.wav` will play on device 1 etc.

Right now, the project only supports debian-based Linux, and the USB-AUDIO from Plugable, which is based on the C-Media HS 100B. It would be very easy to support more devices, make an issue or just send a PR.


## Prerequisites

This project is based on the [sounddevice](https://github.com/spatialaudio/python-sounddevice/) python library.

Run the following command to install the prerequisite debian packages:

```
 sudo apt-get install python3-pip python3-numpy libportaudio2 libsndfile1 screen
```

Then install `sounddevice` and `soundfile`.

```
python3 -m pip install sounddevice soundfile
```

## Installation

Not a whole lot to do here, just clone the repo

```
git clone https://github.com/esologic/pear
```

## Run Manually

Run `pear.py` with the command line argument of the folder the sound files are kept in.

All sound files will start playing at the same time, and will restart once the longest one has finished playing.

Example:

```
$ python3 pear.py ./test
```


## Run at Boot

If you want pear to start playing sound as soon as it turns on, you can add the included `runpear.sh` to your crontab.

Edit your crontab with

```
crontab -e
```

The resulting file should contain the following line:

```

```

### Load sound files automatically from USB drive

In a typically art installation use case, you don't want to have to plug in a keyboard and monitor in order to change the audio files that are playing.

This change allows user to swap sound files using a USB thumb drive or the like.

First, create a mount point for the USB drive.

```
sudo mkdir /mnt/usb/
```

Edit your `/etc/fstab`, adding the following line:
```
LABEL=PEAR /mnt/usb vfat defaults,auto,umask=000,users,ro,nofail 0 0
```

Make sure the drive is labeled `PEAR` or fstab won't pick it up.
