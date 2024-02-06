"""! @file Encoder.py
This program is an Encoder reading class where the program is able
to read a 12V Brushed DC motor using a L6206 H-Bridge Motor Driver.
The class initializes the Encoder's pins and Timer to read the Motor's
position.
"""
import pyb
import utime

class Encoder:
    """!
    This class implements a L6206 H-Bridge Motor Controller Shield.
    """
    
    def __init__ (self, ENA, ENB, timer, CHA, CHB):
        """!
        Creates an Encoder class that intializes the Encoder's
        pins and sets the set GPIO Pin Timer and respective channels.
        @param ENA GPIO pin associated with Encoder Channel A.
        @param ENB GPIO pin associated with Encoder Channel B.
        @param timer Timer for the Encoder.
        @param CHA Timer Channel corresponding to Encoder Channel A.
        @param CHB Timer Channel corresponding to Encoder Channel B.
        @param lastCount Most recent Encoder count.
        @param totalCount Total Encoder count.
        """
        self.pinENA = pyb.Pin(ENA, pyb.Pin.IN)
        self.pinENB = pyb.Pin(ENB, pyb.Pin.IN)
        
        self.tim = pyb.Timer(timer, prescaler = 0, period = 65535)
        self.ENCA = self.tim.channel(CHA, pyb.Timer.ENC_A, pin=ENA)
        self.ENCB = self.tim.channel(CHB, pyb.Timer.ENC_B, pin=ENB)
        self.lastCount = 0
        self.totalCount = 0
        
    def read(self):
        """!
        Function reads the Encoder's position as a positive/negative integer.
        Accounts for under- and over-flow cases by comparing the most recent
        and current count from the Encoder.
        @param count Current Encoder count.
        @param d Changes from last Encoder Count to the most recent Encoder count.
        """
        count = self.tim.counter()
        d = count-self.lastCount
        if d >= 32768:
            d = d-65536
            
        elif d <= -32768:
            d = d+65536
            
        self.totalCount += d
        self.lastCount = count
        return self.totalCount
        
    
    def zero(self):
        """!
        Function set all Encoder counts to 0.
        """
        self.tim.counter(0)
        self.totalCount = 0
        self.lastCount = 0
        

# if __name__ == "__main__":
#     coder = Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4, 1, 2)
#     while True:
#         print(coder.read())
#         utime.sleep(.1)
# #         coder.zero()