class Solution:
    # Date Solved: 7 April 2026, Tuesday
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        """
        This is actually a 0/1 Knapsack Problem
        Weight (w): The present[i] price. This is what it "costs" to take the item.
        Value (v): The profit, which is future[i] - present[i]. If this is less than 0, just ignore the stock.
        Capacity (W): Budget
        """
        dp = [0] * (budget + 1)
        
        for i in range(len(present)):
            cost = present[i]
            profit = future[i] - present[i]
            
            # Only consider stocks that actually make money
            if profit > 0:
                # Iterate backwards to avoid using the same stock twice
                for w in range(budget, cost - 1, -1):
                    dp[w] = max(dp[w], dp[w - cost] + profit)
                    
        return dp[budget]