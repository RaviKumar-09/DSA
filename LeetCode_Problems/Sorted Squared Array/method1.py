# Method 1 Big O Analysis
# brute force for give Sorted Squared Array
def sorted_squared(array):
    n = len(array)
    res = []*n
    for i in range(n):
        res[i] = array[i] ** 2
    res.sort()
    return res
