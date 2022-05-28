import numpy as np

class FP16:
    fpValue = float()
    sign = int()
    exponent = int()
    mantisa = int()

    def __init__(self, value):
        self.fpValue = value
        h = str(bin(np.float16(self.fpValue).view('H'))[2:].zfill(16))
        self.sign = int(h[0],2) # pierwszy bit na znak
        self.exponent = int(h[1]+h[2]+h[3]+h[4]+h[5],2) # nastepne 5 na eksponente
        self.mantisa = int(h[6:],2) # nastepne 10 (od 6 do konca) na mantyse


    def printIEEE(self):
        print(str(bin(self.sign)[2:]),end=' ') # [2:] zeby uciac 0b ktore zwraca bin()
        print(str(bin(self.exponent)[2:]),end=' ')
        print(str(bin(self.mantisa)[2:]))

    def ieee_to_float(self):
        return (-1) ** self.sign * 2 ** (self.exponent - 15) * (1 + self.mantisa/1024)

        
