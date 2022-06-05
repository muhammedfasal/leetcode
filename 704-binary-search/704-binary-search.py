class Solution:
    def search(self, nums: List[int], target: int) -> int:
        _min = 0
        _max = len(nums)-1
        
        while _max >= _min:
            mid = (_max + _min)//2
            
            if nums[mid] > target:
                _max = mid - 1
            elif nums[mid] < target:
                _min = mid + 1
            else:
                return mid
        return -1
                