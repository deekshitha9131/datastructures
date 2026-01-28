def rotate(arr):
    n = len(arr)
    last = arr[-1]
    for i in range(n):
        arr[i] = arr[i-1]
        # arr[0] = last
    return arr
arr = [2,6,4,1,9]
print(rotate(arr))