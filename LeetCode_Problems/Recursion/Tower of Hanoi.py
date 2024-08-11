def toh(N, fromm, to, aux):
    #code below
    # sample print statements below
    #print("move disk" + 1 + "from rod" + 1+ "to rod" + 2)
    # remeber to return number of moves as well
    count = 0
    def helper(N, fromm, to, aux):
        nonlocal count
        # base case
        if N == 1:
            print("move disk" + str[N] + "from rod" + str[fromm] + "to rod" + str[to])
            count += 1
            return
        # recursive case
        helper(N-1,fromm,aux,to)
        print("move disk" + str[N] + "from rod" + str[fromm] + "to rod" + str[to])
        count +=1
        helper(N-1,aux,to,fromm)
    helper(N,fromm,to,aux)

    

    return count