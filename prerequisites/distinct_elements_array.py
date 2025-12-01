def countDistinctElements(arr,n):
    count = 0
    distinct = []
    for i in range(n):
        if arr[i] not in distinct:
            distinct.append(arr[i])
            count += 1
    return count,distinct

if __name__ == "__main__":
    arr = [1, 2, 1, 3, 4, 2, 3]
    n = len(arr)
    count, distinct=countDistinctElements(arr,n)
    print(f"Number of distinct elements are {count}")
    print(f"Distinct elements are {distinct}")