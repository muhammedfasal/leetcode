class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        for indx,num in enumerate(nums):
            sum_value = sum(nums[:indx+1])
            out.append(sum_value)
        return out
            