number= int(input("Enter a natural number: "))
sum=0
for i in range(1, number+1):
    sum += i
print("The sum of natural numbers up to", number, "is:", sum)