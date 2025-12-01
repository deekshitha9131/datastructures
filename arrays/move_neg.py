def move_neg(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:                                               
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1
    return arr
if __name__ == "__main__":
    arr = [1,0,5,3,0,0,2,0]
    res = move_neg(arr)
    print(res)
