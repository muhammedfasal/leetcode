class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currmax = 0
        globalmax = 0
        for i in range(1,len(prices)):
            currmax = max(currmax+(prices[i]-prices[i-1]),0)
            globalmax = max(globalmax,currmax)
        return globalmax