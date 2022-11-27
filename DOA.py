from tuning_soundTact import Tuning
import usb.core
import usb.util
import time
import serial

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
arduino = serial.Serial(port='COM5', baudrate=115200, timeout=10)

if dev:
    Mic_tuning = Tuning(dev)
    arduino.write((str(Mic_tuning.direction) + ' ' + str(int(Mic_tuning.loudness()))).encode('utf-8'))
    while True:
        try:
            arduino.write((str(Mic_tuning.direction) + ' ' + str(int(Mic_tuning.loudness()))).encode('utf-8'))
            time.sleep(0.05)
        except KeyboardInterrupt:
            break
