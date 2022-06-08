import FP16
import LNS

number1 = FP16.FP16(2.0)
number2 = FP16.FP16(3.75)

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

print('MUL (num1*num2):', number1.fpValue * number2.fpValue)
print('MUL IEEE: ', FP16.MUL(number1,number2))
print('LMUL: ', LNS.LMUL(number1,number2), '\n')

print('DIV (num1/num2): ', number1.fpValue / number2.fpValue)
print('DIV IEEE: ', FP16.DIV(number1, number2))
print('LDIV: ', LNS.LDIV(number1, number2), '\n')

print('SR (sqrt(num1)): ', number1.fpValue ** 0.5)
print('SR IEEE: ', FP16.SR(number1))
print('LSR: ', LNS.LSR(number1),'\n')

print('ISR (1/sqrt(num1)): ', 1 / (number1.fpValue ** 0.5))
print('ISR: ', FP16.ISR(number1))
print('LISR: ', LNS.LISR(number1))
