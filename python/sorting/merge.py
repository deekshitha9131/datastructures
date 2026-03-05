def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_subarr = arr[:mid]
        right_subarr = arr[mid:]

        merge_sort(left_subarr)
        merge_sort(right_subarr)

        i = j = k = 0
        while i < len(left_subarr) and j < len(right_subarr):
            if left_subarr[i] < right_subarr[j]:
                arr[k] = left_subarr[i]
                i += 1
            else:
                arr[k] = right_subarr[j]
                j += 1
            k += 1
        while i < len(left_subarr):
            arr[k] = left_subarr[i]
            i += 1
            k += 1
        while j < len(right_subarr):
            arr[k] = right_subarr[j]
            j += 1
            k += 1
result=[38, 27, 43, 3, 9, 82, 10]
merge_sort(result)
print("Sorted array is ", result)