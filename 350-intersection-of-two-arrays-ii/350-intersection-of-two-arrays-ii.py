from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        counter_dict_nums1 = Counter(nums1)
        
        for num2 in nums2:
            if counter_dict_nums1[num2] > 0:
                counter_dict_nums1[num2] = counter_dict_nums1[num2] - 1
                output.append(num2)
        return output
        