class Solution(object):
    def maxSubArray(self, nums):
        sums = max_sum = nums[0]
        for num in nums[1:]:
            sums = max(num,sums+num)
            max_sum = max(sums,max_sum)
        return max_sum
        