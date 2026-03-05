
def co_prime(a,b):
    def gcd(x,y):
        return x if y == 0 else gcd(y, x%y)
    if gcd(a,b) == 1:
        print(f"{a} and {b} are coprime numbers")
    else:
         print(f"{a} and {b} are not coprime numbers")

if __name__ == "__main__":
    co_prime(16, 28)



# if gcd of two numbers is 1 then they are coprime numbers