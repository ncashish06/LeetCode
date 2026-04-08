class Solution:
    # Date Solved: 7 April 2026, Tuesday
    """
    2D DP table to track the maximum profit for every possible number of transactions up to k.
    Time Complexity: O(n * k) - We iterate through prices for each possible transaction.
    Space Complexity: O(k) - We store the minimum buy cost and max profit for k transactions.
    """
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0

        num_days = len(prices)

        # Optimization: If k is large enough, we can perform as many transactions as we want.
        # This effectively becomes 'Best Time to Buy and Sell Stock II'.
        if k >= num_days // 2:
            total_profit = 0
            for i in range(1, num_days):
                if prices[i] > prices[i - 1]:
                    total_profit += prices[i] - prices[i - 1]
            return total_profit

        # effective_buy_cost[i]: The lowest price paid for the i-th transaction,
        # accounting for profits made in the (i-1)-th transaction.
        # 1-based indexing for logic. With k+1, the indices match the transaction count
        min_buy_costs = [float("inf")] * (k + 1)

        # max_profits[i]: The maximum profit achievable after the i-th sell.
        # For k transactions, stores the state of the 0th, 1st, 2nd... all the way to the k-th transaction.
        max_profits = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):  # 1 because can't complete 0 transactions to make a profit.
                # We want to minimize the 'effective cost'.
                # This is the current price minus the profit we already have from the previous transaction.
                min_buy_costs[i] = min(min_buy_costs[i], price - max_profits[i - 1])

                # We want to maximize the profit for the i-th transaction.
                # Current price minus our effective cost for this specific transaction.
                max_profits[i] = max(max_profits[i], price - min_buy_costs[i])

        return max_profits[k]
