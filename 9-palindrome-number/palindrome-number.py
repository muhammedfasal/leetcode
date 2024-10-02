class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_x = 0
        num = x
        while num !=0:
            digit = num%10
            reversed_x = reversed_x * 10 + digit
            num//=10
        return x==reversed_x