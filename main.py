import argparse
import FP16
import LNS
import numpy as np


def num_display(num: FP16):
    print('NUMBER 1: ', num.fpValue)
    print('FP16: ', end='')
    num.printIEEE()
    print('IEEE TO FLOAT: ', num.ieee_to_float())
    print('LNS TO FLOAT: ', LNS.lns_to_float(num), '\n')
    pass


def main():
    parser = argparse.ArgumentParser(description='IEEE754 and LNS arithmetic')

    parser.add_argument('number1', metavar='a',
                        type=float, help='First number')
    parser.add_argument('operation', type=str,
                        choices=['mul', 'div', 'sr', 'isr'], help='Operation')
    parser.add_argument('number2', metavar='b',
                        type=float, help='Second number')

    args = parser.parse_args()

    num1 = FP16.FP16(args.number1)
    operation = args.operation
    num2 = FP16.FP16(args.number2)

    match operation:
        case 'mul':
            print('MUL:', num1.fpValue * num2.fpValue)
            print('MUL IEEE: ', FP16.MUL(num1, num2))
            print('LMUL: ', LNS.LMUL(num1, num2), '\n')

        case 'div':
            FP16.DIV(num1, num2)
            LNS.LDIV(num1, num2)

            print('DIV: ', num1.fpValue / num2.fpValue)
            print('DIV IEEE: ', FP16.DIV(num1, num2))
            print('LDIV: ', LNS.LDIV(num1, num2), '\n')

        case 'sr':
            LNS.LSR(num1)

            print('SR: ', np.float16(num1.fpValue ** 0.5))
            print('SR IEEE: ', FP16.SR(num1))
            print('LSR: ', LNS.LSR(num1), '\n')

        case 'isr':
            print('ISR: ',
                  np.float16(1 / (num1.fpValue ** 0.5)))
            print('ISR: ', FP16.ISR(num1))
            print('LISR: ', LNS.LISR(num1))

        case _:
            pass


if __name__ == "__main__":
    main()
