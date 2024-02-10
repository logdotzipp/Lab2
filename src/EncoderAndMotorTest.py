"""! @file EncoderAndMotorTest.py
This program tests the Encoder class by running a DC motor at a speed and reading the encoder count.
The motor is run with a Motor Driver class.
"""
import pyb
import micropython
from motor_driver import MotorDriver
from Encoder import Encoder
import utime

if __name__ == "__main__":
    
    try:
        # Setup Motor Object
        motor1 = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, pyb.Timer(3, freq=20000))
        # Setup Encoder Object
        coder = Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4, 1, 2)
        
        while True:
            # Run Motor
            motor1.set_duty_cycle(-40)
            utime.sleep(1)
            while True:
                # Read the encoder value and print it
                print(coder.read())
                # Pause so as not to overrun console
                utime.sleep(.1)

    except(KeyboardInterrupt):
        print("Program Terminated")