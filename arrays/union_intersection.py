def union(arr1, arr2):
    result = list(set(arr1) | set(arr2))
    return result
def intersection(arr1, arr2):
    result = list(set(arr1) & set(arr2))
    return result
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [4, 5, 6, 7, 8]
    print("Union:", union(arr1, arr2))
    print("Intersection:", intersection(arr1, arr2))