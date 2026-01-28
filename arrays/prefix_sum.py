def prefix(arr):
    n = len(arr)
    sum = 0
    for i in range(n):
        sum += arr[i]
        arr[i] = sum
    return arr
arr = [1,2,3,4,5]
print(prefix(arr))