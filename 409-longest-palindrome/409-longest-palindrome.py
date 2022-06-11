class Solution:
    def longestPalindrome(self, s: str) -> int:        
        _counter = Counter(s)
        output = 0
        
        for key, value in _counter.items():
            output += 2*(value//2)
            if output % 2 == 0 and value % 2 ==1:
                output += 1
        return output