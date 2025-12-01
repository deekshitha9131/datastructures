def maxWater(arr):
    result = 0
    n = len(arr)
    for i in range(1, n-1):
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])
        right = arr[i]
        for j in range(i+1, n):
            right = max(right, arr[j])
        result += min(left, right) - arr[i]
    return result
if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
    print("Maximum water that can be trapped is:", maxWater(arr))