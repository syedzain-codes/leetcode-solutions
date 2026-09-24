class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minvalue=prices[0]
        for i in prices:
            minvalue=min(minvalue,i)
            maxprofit=max(maxprofit,i-minvalue)
        return maxprofit

        