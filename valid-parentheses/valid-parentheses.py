class Solution:
    def isValid(self, s: str) -> bool:
        k = s
        for i in range(len(s)):
            if k:
                k = k.replace('{}','').replace('[]','').replace('()','')
            else:
                return True
        return False
        