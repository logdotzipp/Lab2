import pyb
import utime

class Encoder:
    
    
    def __init__ (self, ENA, ENB, timer, CHA, CHB):
        
        self.pinENA = pyb.Pin(ENA, pyb.Pin.IN)
        self.pinENB = pyb.Pin(ENB, pyb.Pin.IN)
        
        self.tim = pyb.Timer(timer, prescaler = 0, period = 65535)
        self.ENCA = self.tim.channel(CHA, pyb.Timer.ENC_A, pin=ENA)
        self.ENCB = self.tim.channel(CHB, pyb.Timer.ENC_B, pin=ENB)
        self.lastCount = 0
        self.totalCount = 0
        
    def read(self):
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
        self.tim.counter(0)
        self.totalCount = 0
        self.lastCount = 0
        

# if __name__ == "__main__":
#     coder = Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4, 1, 2)
#     while True:
#         print(coder.read())
#         utime.sleep(.1)
# #         coder.zero()