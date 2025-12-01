def lcm(a,b):
    g= max(a,b)
    s= min(a,b)
    for i in range(g,a*b+1,g):
        if i % s == 0:
            return i
    return a*b
if __name__ == "__main__":
    print(lcm(3,4))


# For a = 4, b = 6,
# range becomes range(6, 25, 6) → [6, 12, 18, 24]
# 6 % 4 != 0
# 12 % 4 == 0 → return 12