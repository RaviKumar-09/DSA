def permute(nums):
    #write code here
    n = len(nums)
    res = []
    def helper(index):
        #base case
        if index == n-1:
            res.append(nums[:])
            return
        #recursive case
        for j in range(index,n):
            nums[index],nums[j] = nums[j], nums[index]
            helper(index+1)
            nums[index],nums[j] = nums[j],nums[index]
    helper(0)
    return res
