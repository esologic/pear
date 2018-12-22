import sounddevice as sd
import soundfile as sf
import threading


def get_device_number_if_usb_soundcard(index_info):
    """
    Given a device dict, return True if the device is one of our USB sound cards and False if otherwise
    :param device: a device info dict from PyAudio.
    :return: True if usb sound card, False if otherwise
    """

    index, info = index_info

    if "USB Audio Device" in info["name"]:
        return index
    return False


def play_wav_on_index(wav_file_path, device_index):
    data, fs = sf.read(wav_file_path, dtype='float32')
    sd.play(data, fs, device=device_index)
    sd.wait()


if __name__ == "__main__":

    usb_sound_card_indicies = filter(lambda x: x is not False,
                                     map(get_device_number_if_usb_soundcard,
                                         [index_info for index_info in enumerate(sd.query_devices())]))

    threads = [threading.Thread(target=play_wav_on_index, args=["test.wav", i]) for i in usb_sound_card_indicies]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
