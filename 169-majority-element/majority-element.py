class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_ = {}
        majority = res = 0
        for i in nums:
            dict_[i] = 1 + dict_.get(i,0)
            if dict_[i] > majority:
                res = i
                majority = dict_[i]
        return res
        