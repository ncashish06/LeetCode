class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_so_far = 0
        min_value_so_far = prices[0]
        n = len(prices)
        for i in range(1, n): 
            min_value_so_far = min(min_value_so_far, prices[i])
            max_profit_so_far = max(max_profit_so_far, prices[i] - min_value_so_far)
        return max_profit_so_far
            