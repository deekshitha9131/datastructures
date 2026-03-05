def second_largest(arr):
    n = len(arr)
    arr.sort()
    return arr[n-2]
# if no elements are same
if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    res = second_largest(arr)
    print(f"The second largest element is {res}")


# for i in range(n - 2, -1, -1):
#     if arr[i] != arr[n - 1]:
#         return arr[i]