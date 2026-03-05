def rotate_array(arr):
    n = len(arr)
    if n == 0:
        return arr
    last_element = arr[-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last_element
    return arr
if __name__ == "__main__":
    arr = [1, 2, 3,8,9,7]
    rotated_arr = rotate_array(arr)
    print("Rotated array:", rotated_arr)