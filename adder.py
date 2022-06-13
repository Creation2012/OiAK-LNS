def full_adder(a, b, cin):
    s = (a ^ b) ^ cin
    c = ((a ^ b) & cin) | (a & b)
    return s, c

def adder_tree(num1,num2):
    result = []
    c = 0

    num1 = [int(x,2) for x in num1] 
    num2 = [int(x,2) for x in num2]

    for i, (n1,n2) in enumerate(zip(reversed(num1), reversed(num2))):
        s,c = full_adder(n1,n2,c)
        result.insert(0,s)

    result.insert(0,c)

    return ''.join(str(x) for x in result)

#num1 = bin(2048)[2:].zfill(13)
#num2 = bin(269)[2:].zfill(13)

#print(int(adder_tree(num1,num2),2))
