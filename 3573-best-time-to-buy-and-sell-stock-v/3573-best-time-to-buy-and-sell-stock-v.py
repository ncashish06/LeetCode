class Solution:
    # Date Solved: 8 April 2026, Wednesday
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2 or k == 0:
            return 0

        # Initialize states
        # Entry: Current max balance if we are "in" a trade
        # Exit: Current max balance if we are "out" of a trade
        long_entry = [-float("inf")] * (k + 1)
        long_exit = [0] * (k + 1)
        short_entry = [-float("inf")] * (k + 1)
        short_exit = [0] * (k + 1)

        for p in prices:
            # We need to copy the previous states to ensure we don't
            # buy and sell on the exact same day.
            prev_long_entry = long_entry[:]
            prev_long_exit = long_exit[:]
            prev_short_entry = short_entry[:]
            prev_short_exit = short_exit[:]

            for i in range(1, k + 1):
                # 1. Entry states: Can start a trade if we were 'out' of a trade yesterday
                # We take the max of either being in a Long or Short trade previously
                prev_best_exit = max(prev_long_exit[i - 1], prev_short_exit[i - 1])

                long_entry[i] = max(prev_long_entry[i], prev_best_exit - p)
                short_entry[i] = max(prev_short_entry[i], prev_best_exit + p)

                # 2. Exit states: Can finish a trade only if we were already 'in' one yesterday
                long_exit[i] = max(prev_long_exit[i], prev_long_entry[i] + p)
                short_exit[i] = max(prev_short_exit[i], prev_short_entry[i] - p)

        return max(long_exit[k], short_exit[k])
