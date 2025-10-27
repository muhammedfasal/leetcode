class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter1, counter2 = {}, {}
        for i in s:
            counter1[i] = counter1.get(i,0)+1
        for i in t:
            counter2[i] = counter2.get(i,0)+1
        return counter1 == counter2
        