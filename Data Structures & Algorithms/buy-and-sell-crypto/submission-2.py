class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r=1
        mini = prices[0]
        max_profit = 0
        while r<len(prices):
            profit = prices[r]-mini
            if prices[r]<mini:
                mini=prices[r]
            max_profit=max(max_profit, prices[r]-mini)
            r+=1
        return max_profit