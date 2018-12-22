# PEAR - a simple tool for sound installations.

Take a directory with `.wav` files named in numeric order
and play them over usb sound devices attached to the host computer.

Right now, the project only supports debian-based Linux, and the USB-AUDIO from Plugable, which is based on the C-Media HS 100B. It would be very easy to support more devices, make an issue or just send a PR.

## Prerequisites

This project is based on the [sounddevice](https://github.com/spatialaudio/python-sounddevice/) python package, which can be tricky to install.

Run the following command to install the prerequisite debian packages:

```
 sudo apt-get install python3-dev python3-pyaudio libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
```

Then install pyaudio

```
python3 -m pip install pyaudio
```

## Usage

Run `pear.py` with the command line argument of the folder the sound files are kept in.

All sound files will start playing at the same time, and will restart once the longest one has finished playing.

Example:

```
$ python3 pear.py ./test
```


