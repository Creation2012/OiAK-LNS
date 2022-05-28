import FP16

number1 = FP16.FP16(6.9)
number2 = FP16.FP16(3.0)

print('Wartosc liczby: ' + str(number1.fpValue)) 
print('FP16: ', end='') 
number1.printIEEE()
print('IEEE TO FLOAT: ' + str(number1.ieee_to_float()))

print('Wartosc liczby: ' + str(number2.fpValue))
print('FP16: ', end='')
number2.printIEEE()
print('IEEE TO FLOAT: ' + str(number2.ieee_to_float()))
