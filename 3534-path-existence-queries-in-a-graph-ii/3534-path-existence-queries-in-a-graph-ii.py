class Solution:
    # Date Solved: 10 July 2026, Friday, POTD
    # Refer: Claude
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        
        order = sorted(range(n), key=lambda i: nums[i])
        sortedVals = [nums[i] for i in order]
        pos = [0] * n  # pos[original_node] = rank in sorted order
        for rank, node in enumerate(order):
            pos[node] = rank

        far = [0] * n
        right = 0
        for i in range(n):
            if right < i:
                right = i
            while right + 1 < n and sortedVals[right + 1] - sortedVals[i] <= maxDiff:
                right += 1
            far[i] = right

        comp = [0] * n
        for i in range(1, n):
            comp[i] = comp[i - 1] + (
                1 if sortedVals[i] - sortedVals[i - 1] > maxDiff else 0
            )

        LOG = max(1, n.bit_length())
        jump = [[0] * LOG for _ in range(n)]
        for i in range(n):
            jump[i][0] = far[i]
        for j in range(1, LOG):
            for i in range(n):
                jump[i][j] = jump[jump[i][j - 1]][j - 1]

        def min_jumps(i: int, target: int) -> int:
            # minimum hops to get from position i to a position >= target
            steps = 0
            cur = i
            for j in range(LOG - 1, -1, -1):
                if jump[cur][j] < target:
                    cur = jump[cur][j]
                    steps += 1 << j
            if cur < target:  # one final hop needed
                cur = jump[cur][0]
                steps += 1
            return steps

        answer = []
        for u, v in queries:
            pu, pv = pos[u], pos[v]
            if pu == pv:
                answer.append(0)
            elif comp[pu] != comp[pv]:
                answer.append(-1)
            else:
                lo, hi = min(pu, pv), max(pu, pv)
                answer.append(min_jumps(lo, hi))

        return answer
