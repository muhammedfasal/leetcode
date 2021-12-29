class Solution:
    def romanToInt(self, S: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        summ= 0
        for i in range(len(S)-1,-1,-1):
            num = roman[S[i]]
            if 3*num < summ: 
                summ = summ-num
            else: 
                summ = summ+num
        return summ