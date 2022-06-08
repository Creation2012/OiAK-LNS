import FP16
import LNS

number1 = FP16.FP16(2.15)
number2 = FP16.FP16(-1.5)
result = FP16

print('Wartosc liczby: ', number1.fpValue) 
print('FP16: ', end='') 
number1.printIEEE()
print('IEEE TO FLOAT: ', number1.ieee_to_float())
LNS1 = LNS.LNS(number1)

print('Wartosc liczby: ', number2.fpValue)
print('FP16: ', end='')
number2.printIEEE()
print('IEEE TO FLOAT: ', number2.ieee_to_float())

#print('DIV: ', FP16.DIV(number1, number2))
#print('LDIV: ', FP16.LDIV(number1,number2))
#print('SR: ', FP16.SR(number1))
#print('ISR: ', FP16.ISR(number1))



