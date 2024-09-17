class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hash_map = {}

        for idx in range(len(nums)):
            if nums[idx] in hash_map and abs(idx - hash_map[nums[idx]]) <= k:
                return True
            hash_map[nums[idx]] = idx
