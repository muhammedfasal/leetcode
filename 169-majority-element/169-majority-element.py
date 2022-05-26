class Solution(object):
    def majorityElement(self, nums):
        dict1 = Counter(nums)
        return max(dict1, key=dict1.get)
        