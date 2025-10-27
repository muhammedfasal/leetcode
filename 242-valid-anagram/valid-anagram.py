class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1, counter2 = {}, {}
        for i in s:
            counter1[i] = counter1.get(i,0)+1
        for i in t:
            counter2[i] = counter2.get(i,0)+1
        if counter1 == counter2:
            return True
        return False
        