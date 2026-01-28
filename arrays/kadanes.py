# subarray with maximum sum
def maxSubArray(arr):
    result = arr[0]
    n = len(arr)
    for i in range(n):
        currSum = 0    #currSum is always updated to 0
        for j in range (i,n):
            currSum += arr[j]
            if currSum > result:
                result = currSum
                start = i
                end = j
    return result, arr[start:end+1]
if __name__ == "__main__":
    arr = [2,3,-8,7,-1,2,3]
    max_sum, subarray = maxSubArray(arr)
    print("Maximum subarray sum is:", max_sum)
    print("The subarray is:", subarray)
