def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    #return -1

arr=list(map(int,input("Enter the elements of array separated by space:").split()))
target=int(input("Enter the target element:"))
result=binary_search(arr,target)
print("Element found at index:",result)