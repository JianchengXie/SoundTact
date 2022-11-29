from tuning_soundTact import Tuning
import usb.core
import usb.util
import time
import serial
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 3  # Duration of recording
dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
arduino = serial.Serial(port='COM6', baudrate=115200, timeout=100)


def recording():
    data = arduino.readline()
    switch = 0
    if data:
        data_decoded = data.decode()
        switch = data_decoded.rstrip()
        print(switch)
    return switch

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print(str(Mic_tuning.direction) + ' ' + str(int(volume_norm)+70))
    arduino.write((str(Mic_tuning.direction) + ' ' + str(int(volume_norm)+70)).encode('utf-8'))

if dev:
    Mic_tuning = Tuning(dev)
    while True:
        try:
            with sd.Stream(callback=print_sound):
                sd.sleep(50)
            arduino.reset_input_buffer()
            arduino.reset_output_buffer()
            time.sleep(0.05)
            record = recording()
            if record:
                record = int(record)
            else:
                continue
            if record == 1:
                print("recording start")
                myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                sd.wait()  # Wait until recording is finished
                print("recording end")
                write('output.wav', fs, myrecording)  # Save as WAV file
        except KeyboardInterrupt:
            break

