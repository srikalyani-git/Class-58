def HCF(a,b):
    while b:
        var = b
        b = a%b
        a = var
    return a

def LCM(a,b):
    print((a*b)/HCF(a,b))

LCM(16,24)