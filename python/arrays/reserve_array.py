#if no temp only half of the array is sorted as we don't update the end elements of array
# so create a temp array of size equals to array size
# update the temp array with reverse elements and copy the temp array elements to original array

def reverseArray(arr):
    n=len(arr)
    temp=[0]*n
    for i in range(n):
        temp[i]=arr[n-1-i]

    for i in range(n):
        arr[i]=temp[i]
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    reverseArray(arr)
    print("Reversed array is:", arr)


# for i in range(n//2):
#         temp = arr[i]
#         arr[i] = arr[n-1-i]
#         arr[n-1-i] = temp     

# rev = arr[::-1]

# arr.reverse()