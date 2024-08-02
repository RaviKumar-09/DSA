def monotonic_array(array):
    n = len(array)
    first = array[0]
    last = array[n-1]

    if first>last:
        #MD or array is not monotonic
        for k in range(n-1):
            if array[k] < array[k+1]:return False
    elif first == last:
        #M-all values are equal
        for k in range(n-1):
            if array[k]!= array[k+1]: return False
    else:
        #first < Last
        #MI or not M
        for k in range(n-1):
            if array[k] > array[k+1]: return False
    return True