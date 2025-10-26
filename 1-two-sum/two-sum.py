class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            m = target - num
            if m in hashmap:
                return [idx, hashmap[m]]
            else:
                hashmap[num] = idx
        