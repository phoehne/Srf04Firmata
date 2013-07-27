from pyfirmata import Board, util, BOARDS
from time import sleep

#("/dev/tty.usbmodemfa131")

SRF04_MESSAGE = 0x40

class MyArduino(Board):
    def __init__(self, *args, **kwargs):
        args = list(args)
        args.append(BOARDS['arduino'])
        super(MyArduino, self).__init__(*args, **kwargs)

    def pingSrf04(self, echo, trigger):
        self.sp.write(chr(SRF04_MESSAGE))
        self.sp.write(chr(echo))
        self.sp.write(chr(trigger))

        print "wrote bytes"

        return [hex(ord(self.sp.read(1))), hex(ord(self.sp.read(1))), hex(ord(self.sp.read(1)))]


if __name__ == "__main__":
    myArduino = MyArduino("/dev/tty.usbmodemfd121")

    print myArduino.get_firmata_version()
    myArduino.digital[13].write(1)
    sleep(1)
    myArduino.digital[13].write(0)

    for i in range(1, 10):
        sleep(1)
        print myArduino.pingSrf04(9, 8)

