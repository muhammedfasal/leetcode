class Solution:
    def reverse(self, x: int) -> int:
        k = abs(x)
        rev = 0
        while (k > 0):
            dig = k%10
            rev = rev * 10 + dig
            k = k//10
        ans = rev if abs(x) == x else (0-rev)
        if ans >= 2 ** 31 - 1 or ans <= -2 ** 31:
            return 0
        return ans