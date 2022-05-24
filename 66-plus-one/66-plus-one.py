class Solution(object):
    def plusOne(self, digits):
        num=int(''.join([str(digit) for digit in digits]))+1
        mylist = [int(d) for d in list(str(num))]
        return mylist