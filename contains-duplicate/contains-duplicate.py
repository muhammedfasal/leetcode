class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        k = set()
        for i in nums:
            if i not in k:
                k.add(i)
            else:
                return True
        return False
        