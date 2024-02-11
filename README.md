# Lab2
 ME 405 Bin 9 Lab 2

 This lab implements an incremental quadrature encoder class using a 16bit counter. The class sets up the timer counter, and then contains functionality read the total encoder count or rezero the encoder.

 Reading the encoder accounts for overflow and underflow of the counter.

 A motor driver class motor_driver.py is also implemented to allow for testing the encoder with a motor with EncoderAndMotorTest.py
