def sumSubarray0(arr):
    sum = arr[0]
    n = len(arr)
    for i in range(n):
        sum = arr[i]
        if sum == 0:
            return True
        for j in range(i+1, n):
            sum += arr[j]
            if sum == 0:
                return True
    return False
     
if __name__ == "__main__":
    arr = [4, 2, -3, 1, 6]
    if sumSubarray0(arr):
        print("Subarray with sum 0 exists")
    else:
        print("Subarray with sum 0 does not exist")