import FP16
import LNS
import random
import numpy as np
import csvData
import time

def gen():
    for i in range(0,100):
        number1 = FP16.FP16(random.uniform(0.1,5.0))
        number2 = FP16.FP16(random.uniform(0.1,5.0))
        #csvData.dataToFile(number1.fpValue, number2.fpValue, np.float16(LNS.lns_to_float(number1)), np.float16(LNS.lns_to_float(number2)))
        stdiv = time.perf_counter()
        div = number1.fpValue / number2.fpValue
        enddiv = time.perf_counter()
        stldiv = time.perf_counter()
        ldiv = LNS.LDIV(number1,number2)
        endldiv = time.perf_counter()

        stsr = time.perf_counter()
        sr =  number1.fpValue ** 0.5
        endsr = time.perf_counter()
        stlsr = time.perf_counter()
        lsr = LNS.LSR(number1)
        endlsr = time.perf_counter()

        csvData.dataToFile((enddiv - stdiv) * 1000, (endldiv - stldiv) * 1000, (endsr - stsr) * 1000, (endlsr - stlsr) * 1000)
    return 

def gen_lns():
    for i in range(0,100):
        number1 = FP16.FP16(random.uniform(0.1,5.0))
        number2 = FP16.FP16(random.uniform(0.1,5.0))

def example():
    number1 = FP16.FP16(0.75)
    number2 = FP16.FP16(0.25)

    print('NUMBER 1: ', number1.fpValue) 
    print('FP16: ', end='') 
    number1.printIEEE()
    print('IEEE TO FLOAT: ', number1.ieee_to_float())
    print('LNS TO FLOAT: ', LNS.lns_to_float(number1), '\n')

    print('NUMBER 2: ', number2.fpValue)
    print('FP16: ', end='')
    number2.printIEEE()
    print('IEEE TO FLOAT: ', number2.ieee_to_float())
    print('LNS TO FLOAT: ', LNS.lns_to_float(number2), '\n')

    stdiv = time.perf_counter()
    print('MUL (num1*num2):', number1.fpValue * number2.fpValue)
    enddiv = time.perf_counter()
    stldiv = time.perf_counter()
    print('MUL IEEE: ', FP16.MUL(number1,number2))
    endldiv = time.perf_counter()
    print('LMUL: ', LNS.LMUL(number1,number2), '\n')

    #print('MUL TIME: ', enddiv - stdiv)
    #print('LMUL TIME: ', endldiv - stldiv,'\n')

    value1 = number1.fpValue
    value2 = number2.fpValue
    stdiv = time.perf_counter()
    x = FP16.DIV(number1,number2)
    enddiv = time.perf_counter()
    stldiv = time.perf_counter()
    LNS.LDIV(number1,number2)
    endldiv = time.perf_counter()

    print('DIV (num1/num2): ', number1.fpValue / number2.fpValue)
    print('DIV IEEE: ', FP16.DIV(number1, number2))
    print('LDIV: ', LNS.LDIV(number1, number2), '\n')

    print('DIV TIME: ',(enddiv - stdiv) * 1000)
    print('LDIV TIME: ',(endldiv - stldiv) * 1000,'\n')

    value = number1.fpValue
    stsr = time.perf_counter()
    value ** 0.5
    endsr = time.perf_counter()
    stlsr = time.perf_counter()
    LNS.LSR(number1)
    endlsr = time.perf_counter()

    print('SR (sqrt(num1)): ', np.float16(number1.fpValue ** 0.5))
    print('SR IEEE: ', FP16.SR(number1))
    print('LSR: ', LNS.LSR(number1),'\n')

    print('SR TIME: ', (endsr - stsr) * 1000)
    print('LSR TIME: ', (endlsr - stlsr) * 1000,'\n')

    print('ISR (1/sqrt(num1)): ', np.float16(1 / (number1.fpValue ** 0.5)))
    print('ISR: ', FP16.ISR(number1))
    print('LISR: ', LNS.LISR(number1))
