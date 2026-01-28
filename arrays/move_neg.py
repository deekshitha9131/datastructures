# two pointers
# Check the condition and update the pointers
def move_negatives(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] < 0:
            left += 1
            print("Left",left)
        elif arr[right] >= 0:
            right -= 1
            print("right",right)
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

if __name__ == "__main__":
    arr = [4,-1,-2,0,-3,8,-5]
    res = move_negatives(arr)
    print(res)
