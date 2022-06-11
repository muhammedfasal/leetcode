class Solution:
    def longestPalindrome(self, s: str) -> int:        
        c = Counter(s)
        res = 0
        for k, count in c.items():
            res += count // 2
        return res*2 + (len(s) > res*2)