def logconverter(mantisa):
    m = mantisa
    if m in range(0,96):
        a = [1,-3]
        b = 13
    elif m in range(96,192):
        a = [2,6]
        b = 98
    elif m in range(192,304):
        a = [3,5]
        b = 269
    elif m in range(304,416):
        a = [4]
        b = 501
    elif m in range(416,560):
        a = [-6]
        b = 763
    elif m in range(560,704):
        a = [-3,6]
        b = 1178
    elif m in range(704,848):
        a = [-2,4]
        b = 1622
    elif m in range(848,1024):
        a = [-2]
        b = 2055

    shifted = m << 3
    shifted += b
    shifted += sum([-1 * (m >> abs(i)) if i < 0 else m >> abs(i) for i in a])
    shifted = shifted >> 3
    
    return shifted

def antilogconverter(mantisa):
    m = mantisa
    print('DEBUG: ', m)
    if m in range(0,160):
        a = [-2,-6]
        b = 8188
    elif m in range(160,288):
        a = [-2,4]
        b = 8085
    elif m in range(288,432):
        a = [-3,6]
        b = 7898
    elif m in range(432,576):
        a = [-5]
        b = 7625
    elif m in range(576,704):
        a = [4,6]
        b = 7123
    elif m in range(704,816):
        a = [3,5]
        b = 6680
    elif m in range(816,944):
        a = [2,6]
        b = 5964
    elif m in range(944,1024):
        a = [1,-3]
        b = 5131

    shifted = m << 3
    shifted += b
    shifted += sum([-1 * (m >> abs(i)) if i < 0 else m >> abs(i) for i in a])
    shifted = shifted >> 3
    
    return shifted

def lns_to_float(num):
    k = logconverter(num.mantisa)/1024
    return (-1)**num.sign * 2 ** (num.exponent - 15) * 2 ** k

def LMUL(num1, num2):
    k1 = logconverter(num1.mantisa)/1024 # bitwise shift? 
    k2 = logconverter(num2.mantisa)/1024
    return (-1) ** num1.sign * (-1) ** num2.sign * 2 ** ((num1.exponent + num2.exponent + k1 + k2) - 30)
    #return (-1) ** num1.sign * (-1) ** num2.sign * 2 ** ((num1.exponent + logconverter(num1.mantisa)/1024) + (num2.exponent + logconverter(num2.mantisa)/1024))

def LDIV(num1, num2):
    k1 = logconverter(num1.mantisa)/1024
    k2 = logconverter(num2.mantisa)/1024
    return (-1) ** num1.sign * (-1) ** num2.sign * 2 ** ((num1.exponent + k1) - (num2.exponent + k2))

def LSR(num1):
    k = logconverter(num1.mantisa)/1024
    return 2 ** (0.5 * (num1.exponent + k) - 7.5)

def LISR(num1):
    k = logconverter(num1.mantisa)/1024
    return 2 ** (-0.5 * (num1.exponent + k) + 7.5)
