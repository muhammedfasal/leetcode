class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for idx, num in enumerate(nums):
            if num in hashmap:
                return True
            hashmap[num] = idx
        return False

