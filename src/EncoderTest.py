"""! @file EncoderTest.py
This program tests the Encoder class by running a DC motor at a speed and reading the encoder count.
Also makes use of the MotorDriver class
"""
import pyb
import micropython
from motor_driver import MotorDriver
from Encoder import Encoder
import utime

if __name__ == "__main__":
    
    try:
        motor1 = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, pyb.Timer(3, freq=20000))
        coder = Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4, 1, 2)
        while True:
            motor1.set_duty_cycle(-40)
            utime.sleep(1)
            while True:
                print(coder.read())
                utime.sleep(.1)


    except(KeyboardInterrupt):
        print("Program Terminated")