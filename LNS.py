class LNS:
    fpValue = float()
    sign = int()
    exponent = int()
    mantisa = int()

    def __init__(self, num):
        self.fpValue = num.fpValue
        self.sign = num.sign
        self.exponent = num.exponent
        self.mantisa = num.mantisa

    def logconverter(self):
        m = self.mantisa
        if m in range(0,95):
            a = [1,-3]
            b = 13
        elif m in range(96,191):
            a = [2,6]
            b = 98
        elif m in range(192,303):
            a = [3,5]
            b = 269
        elif m in range(304,415):
            a = [4]
            b = 501
        elif m in range(416,559):
            a = [-6]
            b = 763
        elif m in range(560,703):
            a = [-3,6]
            b = 1178
        elif m in range(704,847):
            a = [-2,4]
            b = 1622
        elif m in range(848,1023):
            a = [-2]
            b = 2055

        shifted = m << 3
        shifted += b
        shifted += sum([-1 * (m >> abs(i)) if i < 0 else m >> abs(i) for i in a])
        
        return shifted
