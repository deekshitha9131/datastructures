num=2589
sum=0
while num !=0:
    sum += num % 10
    print(sum)
    num = num // 10
print(sum)