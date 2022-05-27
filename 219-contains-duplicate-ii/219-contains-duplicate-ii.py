class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        map_index = {}
        
        for i in range(len(nums)):
            num = nums[i]
            if num in map_index and i - map_index[num]<= k:
                return True
            map_index[num] = i
        return False