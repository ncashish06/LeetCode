class Solution:
    # Date Solved: 7 April 2026, Tuesday
    """
    We need a 2D DP table (or two arrays) to track the maximum profit for every possible number of transactions up to k.
    """

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0

        # If k is very large, it's the same as Part II (unlimited transactions)
        if k >= len(prices) // 2:
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))

        # Track the 'cost' and 'profit' for each of the k transactions
        buy = [float("inf")] * (k + 1)
        sell = [0] * (k + 1)

        for p in prices:
            for i in range(1, k + 1):
                # Update the cost of the i-th purchase
                buy[i] = min(buy[i], p - sell[i - 1])
                # Update the profit of the i-th sale
                sell[i] = max(sell[i], p - buy[i])

        return sell[k]
