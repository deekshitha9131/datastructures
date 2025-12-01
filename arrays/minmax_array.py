def minMaxArray(arr):
    arr.sort()
    minimum = arr[0]
    maximum = arr[-1]
    return minimum, maximum

if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    minimum, maximum = minMaxArray(arr)
    print("Minimum element is:", minimum)
    print("Maximum element is:", maximum)