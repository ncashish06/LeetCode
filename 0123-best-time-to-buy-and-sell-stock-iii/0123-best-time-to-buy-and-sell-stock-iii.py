class Solution:
    # Date Solved: 5 April 2026, Sunday
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0

        for price in prices:
            buy1  = min(buy1, price)# best (min) price to buy first stock
            sell1 = max(sell1, price - buy1) # best (max) profit from txn 1
            buy2  = min(buy2, price - sell1) # best (min) effective cost of 2nd buy, minimize "re-investment" cost
            sell2 = max(sell2, price - buy2) # best (max) profit from both transactions

        return sell2