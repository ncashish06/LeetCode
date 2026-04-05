class Solution:
    # Date Solved: 5 April 2026, Sunday
    def maxProfit(self, prices: List[int]) -> int:
        # Think like a graph with x-y axis and take only positive gradients (be greedy)
        all_profits = 0
        n = len(prices)
        for i in range(1, n):
            curr_profit = prices[i]-prices[i-1]
            if curr_profit>0:
                all_profits+=curr_profit
        return all_profits