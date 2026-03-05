def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i+1
 
arr = [5,4,7,4,2,1,4,3]
key = 1
result = linear_search(arr, key)
print(result)