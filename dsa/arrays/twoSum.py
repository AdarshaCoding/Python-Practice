values = [4, 2, 8, 5, 3, 9]
key = 50


# brute force method
def twoSum(arr, key):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == key:
                return [i, j]
    return "no match found"


results = twoSum(values, key)
print(results)
