def combinationSum(candidates, target):
    #write code here
    res = []
    n = len(candidates)
    def helper(start_index,curr,sum_included):
        #base case
        if sum_included>target:
            return
        if sum_included ==target:
            res.append(curr[:])
        #recursive case
        for j in range(start_index,n):
            
    helper(0,[],0)
    return res