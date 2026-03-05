number1 = int(input("Enter the starting number of the range: "))
number2 = int(input("Enter the ending number of the range: "))
for i in range(number1, number2 + 1):
    if i > 1:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)
