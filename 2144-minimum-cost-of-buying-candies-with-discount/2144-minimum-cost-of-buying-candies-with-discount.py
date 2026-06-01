class Solution:
    # Date Solved: 1 June 2026, Monday, POTD
    def minimumCost(self, cost: List[int]) -> int:
        total_cost = 0
        n = len(cost)
        cost.sort(reverse=True)
        for i in range(n):
            if i % 3 == 2:
                continue
            total_cost += cost[i]
        return total_cost
