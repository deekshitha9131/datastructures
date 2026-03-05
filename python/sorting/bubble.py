def bubble_sort(arr):
    n = len(arr)
    print("Original array")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    for i in range(len(arr)):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1], arr[j] = arr[j],arr[j+1]
    return arr

arr = ([2,4,1,7,4,7,45,3,6,66])
result = bubble_sort(arr)
print("\nSorted array:")
print(result)