from tuning_soundTact import Tuning
import usb.core
import usb.util
import time

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)

if dev:
    Mic_tuning = Tuning(dev)
    print(str(Mic_tuning.direction) + ' ' + str(Mic_tuning.loudness()))
    while True:
        try:
            print(str(Mic_tuning.direction) + ' ' + str(Mic_tuning.loudness()))
            time.sleep(1)
        except KeyboardInterrupt:
            break