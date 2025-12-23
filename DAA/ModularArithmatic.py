def modShow(a,mod):
    return a%mod
def modAdd(a,b,mod):
    
    return (a+b)%mod

def modSubtract(a,b,mod):
    
    return (a-b)%mod

def modMutiply(a,b,mod):
    
    return (a*b)%mod

def modEqual(a,b,mod):
    
    return a%mod == b%mod

def modPow(a, b, mod):
    if b == 0:
        return 1 % mod

    u = modPow(a, b // 2, mod)
    u = (u * u) % mod

    if b % 2 == 1:
        u = (u * a) % mod
    return u

print(modEqual(38,14,12))
print(modAdd(27,19,7))
print(modMutiply(23,17,5))
print(modPow(7,100,11))