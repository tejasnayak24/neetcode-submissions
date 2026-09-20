class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res=0
        for i in range(len(prices)):
            buy=prices[i]
            for j in range(i,len(prices)):
                sell=prices[j]
                res=max(res,sell-buy)
        return res

        