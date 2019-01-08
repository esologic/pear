"""
Blocks until the sounddevice module is able to pick up all of the attached usb sound cards as seen by lsusb
"""

import subprocess


def num_sound_devices():
    """
    Use an external call to sounddevice to get the number of devices detected by the library.
    It's important to do this rather than just sounddevice.query_devices(),
    :return:
    """

    return str(subprocess.check_output(["python3", "-m", "sounddevice"])).count("USB Audio Device")


def wait_for_usb_sound_devices_to_be_initialized():
    """
    Calling this function will block until the number of USB sound soundcard devices detected by lsusb matches
    the number initialized by the sound device backend.
    :return:
    """

    while num_sound_devices() != str(subprocess.check_output(["lsusb"])).count("C-Media Electronics"):
        pass


if __name__ == "__main__":
    wait_for_usb_sound_devices_to_be_initialized()
