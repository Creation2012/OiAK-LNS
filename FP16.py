import numpy as np
import math as m

class FP16:
    fpValue = np.float16()
    sign = int()
    exponent = int()
    mantisa = int()

    def __init__(self, value):
        self.fpValue = np.float16(value)
        h = str(bin(np.float16(self.fpValue).view('H'))[2:].zfill(16))
        self.sign = int(h[0],2) # pierwszy bit na znak
        self.exponent = int(h[1]+h[2]+h[3]+h[4]+h[5],2) # nastepne 5 na eksponente
        self.mantisa = int(h[6:],2) # nastepne 10 (od 6 do konca) na mantyse

    def printIEEE(self):
        print(str(bin(self.sign)[2:]),end=' ') # [2:] zeby uciac 0b ktore zwraca bin()
        print(str(bin(self.exponent)[2:]).zfill(5),end=' ')
        print(str(bin(self.mantisa)[2:]).zfill(10))

    def ieee_to_float(self):
        return np.float16((-1) ** self.sign * 2 ** (self.exponent - 15) * (1 + self.mantisa/1024))
        
def MUL(num1, num2):
    return np.float16((-1)**num1.sign * (-1) ** num2.sign * 2 ** (num1.exponent - 15 + num2.exponent - 15) * (1 + num1.mantisa/1024) * (1 + num2.mantisa/1024))

def DIV(num1, num2):
    return np.float16((-1)**num1.sign * (-1)**num2.sign * 2 ** ((num1.exponent - 15) - (num2.exponent - 15)) * ((1 + num1.mantisa/1024)/(1 + num2.mantisa/1024)))

def SR(num):
    return np.float16(2 ** (0.5 * (num.exponent - 15)) * (1+num.mantisa/1024)**0.5)

def ISR(num):
    return np.float16(SR(num) ** -1)
