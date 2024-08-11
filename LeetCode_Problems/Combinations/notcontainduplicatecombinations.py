def combinationSum2(candidates, target):
    #write code here
    candidates.sort()
    res = []
    n = len(candidates)
    def helper(index,curr,curr_sum):
        #base case
        if curr_sum == target:
            res.append(curr[:])
            return
        if curr_sum > target:
            return
        if index . n-1:
            return
        #recursive case
        hash = {}
        for i in range(index,n):
            if candidates[i] not in hash:
                hash[candidates[i]] = True
                curr.append(candidates[i])
                helper(i+1,curr,curr_sum + candidates[i])
                curr.pop()
    helper(0,[],0)
    return res