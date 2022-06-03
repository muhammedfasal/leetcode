class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = (''.join(filter(str.isalnum, s))).lower()
        if k == k[::-1]:
            return True
        else:
            return False
        