def kth_symbol(n, k):
    #write code Here
    #0
    #01
    #0110
    #base case 
    if n==1:return 0
    length = 2**(n-1)
    mid = length //2
    if k<=mid:
        return kth_symbol(n-1,k)
    else:
        return int(not kth_symbol(n-1,k - mid))
        #return 1- kth_symbol(n-1,k-mid)