def gcd(a,b):
    result = min(a,b)
    while result>0:
        if a % result == 0 and b % result == 0:
            break
        result -=1
    return result
if __name__ == "__main__":
    a=20
    b=28
    print(gcd(a,b))


def gcd1(a,b):
    return a if b==0 else gcd1(b, a%b)
a = 20
b = 24
print(gcd1(a,b))

def gcd2(a, b):
    return math.gcd(a,b)
if __name__ == "__main__":
    import math
    a = 20
    b = 24
    print(gcd2(a, b))


# hcf and gcd are same
