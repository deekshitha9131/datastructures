def next_greater_element(arr):
    n = len(arr)
    result = [-1]*n
    # print(result)
    stack =[]
    for i in range(n-1,-1,-1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result

arr = [4,5,2,25]
print("Next greater elements:")
res= next_greater_element(arr)
for i in range(len(arr)):
    print(f"{arr[i]} --> {res[i]}")