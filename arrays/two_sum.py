def two_sum_sort(arr, tar):
    l = 0
    r = len(arr)-1
    while l<r:
        sum = arr[l] + arr[r]
        if sum == tar:
            return [l,r]
        elif sum < tar:
            l += 1
        else:
            r -= 1
    return 
if __name__ == "__main__":
    arr = [2,3,5,9,11]
    tar = 14
    res = two_sum_sort(arr, tar)
    print(res)
    
