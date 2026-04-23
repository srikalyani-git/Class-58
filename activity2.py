def HCF(a,b):
    while b:
        var = b
        b = a%b
        a = var
    print(a)

HCF(24,16)