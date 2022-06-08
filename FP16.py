import numpy as np
import math as m

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
        print(str(bin(self.exponent)[2:]).zfill(5),end=' ')
        print(str(bin(self.mantisa)[2:]).zfill(10))

    def ieee_to_float(self):
        return (-1) ** self.sign * 2 ** (self.exponent - 15) * (1 + self.mantisa/1024)
        
def MUL(num1, num2):
    return 0

def DIV(num1, num2):
    return 2 ** ((num1.exponent - 15) - (num2.exponent - 15)) * ((1 + num1.mantisa/1024)/(1 + num2.mantisa/1024))

def LDIV(num1,num2):
    k1 = m.log(1 + num1.mantisa/1024, 2)
    k2 = m.log(1 + num2.mantisa/1024, 2)
    return 2 ** ((num1.exponent + k1) - (num2.exponent + k2)) 

def SR(num):
    return 2 ** (0.5 * (num.exponent - 15)) * m.sqrt(1+num.mantisa/1024)

def LSR(num):
    k1 = m.log(1 + num.mantisa/1024, 2)
    return 2 ** (0.5 * (num.exponent + k1) - 7.5)
