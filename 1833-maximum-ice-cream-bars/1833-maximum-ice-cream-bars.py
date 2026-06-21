class Solution:
    # Date Solved: 21 June 2026, Sunday, POTD
    # Refer: codestorywithMIK and Namaste DSA for counting sort code
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)

        # Build count array
        count = [0] * (max_cost + 1)
        for cost in costs:
            count[cost] += 1

        total = 0
        for cost in range(1, max_cost + 1):
            if count[cost] == 0:
                continue
            if coins < cost:
                break

            # Buy as many as possible at this cost
            buy = min(count[cost], coins // cost)
            total += buy
            coins -= buy * cost

        return total
