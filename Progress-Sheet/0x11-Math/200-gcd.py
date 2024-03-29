def gcd(a,b):
    if b == 0:
        return a
    return gcd(b , a % b)



def lcm(a,b):
    return a*b // gcd(a,b)


a = gcd(32,28)
b = lcm(6,10)

print(b,50+16+33)


# a U b U c = a + b + c + a*b*c - (a*b) - (a*c) - (a*d)