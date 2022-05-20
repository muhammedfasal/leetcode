class Solution(object):
    def twoSum(self, nums, target):
        dict1 = {}
        for idx, value in enumerate(nums):
            if target - value in dict1:
                return [dict1[target-value],idx]
            else:
                dict1[value] = idx
        