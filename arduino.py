from pyfirmata import Arduino, util
board = Arduino('/dev/cu.usbserial-1410')

board.digital[3].write(1)