"""
See README.md for usage and installation
Written by Devon Bray (dev@esologic.com)
"""

import sounddevice
import soundfile
import threading
import argparse
import pathlib
import os
import time
import pyaudio
import wave
import numpy as np


def load_sound_file_into_memory(path):
    """
    Get the in-memory version of a given path to a wav file
    TODO: would love the use of a with statement here.
    :param path: wav file to be loaded
    :return: audio_data, sample rate
    """

    return soundfile.read(path, dtype="int16")


def dir_path(path):
    """
    Checks to see if the given path is actually a directory
    :param path: a path to a directory
    :return: path if it's a directory, raises an error if otherwise
    """

    p = pathlib.Path(path)
    if p.is_dir():
        return path
    else:
        raise NotADirectoryError(path)


def get_device_number_if_usb_soundcard(index_info):
    """
    Given a device dict, return True if the device is one of our USB sound cards and False if otherwise
    :param index_info: a device info dict from PyAudio.
    :return: True if usb sound card, False if otherwise
    """

    index, info = index_info

    if "USB Audio Device" in info["name"]:
        return index
    return False


def play_wav_on_index(audio_data_and_sample_rate, index):
    """
    Play an audio file given as the result of `load_sound_file_into_memory`
    :param audio_data_and_sample_rate: (A two-dimensional NumPy array , sample rate)
    :param index: the device index of the output device
    :return: None, returns when the song has finished
    """

    print("Playing audio on device", index)
    audio_data, sample_rate = audio_data_and_sample_rate
    sounddevice.play(audio_data, sample_rate, device=index, blocking=True)
    sounddevice.wait()
    print("Done playing audio on device", index)


def play_wav_on_index_new(audio_data_and_sample_rate, stream_object):
    """
    Play an audio file given as the result of `load_sound_file_into_memory`
    :param audio_data_and_sample_rate: (A two-dimensional NumPy array , sample rate)
    :param index: the device index of the output device
    :return: None, returns when the song has finished
    """
    data, sample_rate = audio_data_and_sample_rate
    stream_object.write(data)


def create_output_stream(index):
    
    output = sounddevice.OutputStream(
        device=index,
        samplerate=44100,
        dtype="int16"
    )
    output.start()
    return output


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='a simple tool for sound installations')
    parser.add_argument("dir", type=dir_path)
    args = parser.parse_args()

    sound_file_paths = [os.path.join(args.dir, path) for path in sorted(filter(lambda path: str(path).endswith(".wav"),
                                                                               os.listdir(args.dir)))]

    print("Discovered the following .wav files:", sound_file_paths)

    files = [load_sound_file_into_memory(path) for path in sound_file_paths]

    print("Files loaded into memory")

    usb_sound_card_indices = list(filter(lambda x: x is not False,
                                         map(get_device_number_if_usb_soundcard,
                                             [index_info for index_info in enumerate(sounddevice.query_devices())])))

    print("Discovered the following usb sound devices", usb_sound_card_indices)

    streams = [create_output_stream(index) for index in usb_sound_card_indices]

    running = True

    p = pyaudio.PyAudio()

    while running:

        print("Playing files")

        try:
            threads = [threading.Thread(target=play_wav_on_index_new, args=[file_path, stream])
                       for file_path, stream in zip(files, streams)]

            for thread in threads:
                thread.start()

            for thread, device_index in zip(threads, usb_sound_card_indices):
                print("Waiting for device", device_index, "to finish")
                thread.join()

        except KeyboardInterrupt:
            running = False
            print("Program will stop when files have finished playing")

    p.terminate()

    print("Bye.")