class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            #is this profitable?

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                #if this isnt profitable, then the left pointer gets shifted
                l = r
            r+= 1
        
        return maxP