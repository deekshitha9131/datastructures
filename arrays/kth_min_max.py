def kth_min_max(arr, k):
    arr.sort()
    print(arr)
    kth_minimum = arr[k-1]
    kth_maximum = arr[-k]
    return kth_minimum, kth_maximum
if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    kth_minimum, kth_maximum = kth_min_max(arr, k)
    print(f"{k}th minimum element is:", kth_minimum)
    print(f"{k}th maximum element is:", kth_maximum)