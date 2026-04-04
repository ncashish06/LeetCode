class Solution:
    # Date Solved: 4 April 2026, Saturday
    def maxProfit(self, prices: List[int]) -> int:
        # Related to Kadane's algo
        # 1D Dynamic Programming
        # Think like a X-Y axis Graph, the answer is the difference between peak(highest) and valley(smallest) in the graph, with peak coming after valley
        max_profit_so_far = 0
        min_value_so_far = prices[0]
        n = len(prices)
        for i in range(1, n):
            min_value_so_far = min(min_value_so_far, prices[i])
            max_profit_so_far = max(max_profit_so_far, prices[i] - min_value_so_far)
        return max_profit_so_far
