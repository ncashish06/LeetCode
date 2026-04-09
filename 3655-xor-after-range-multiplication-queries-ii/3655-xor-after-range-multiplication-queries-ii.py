class Solution:
    # Date Solved: 8 April 2026, Wednesday
    # Time: O((n + q)√n + q log M) where n is the length of nums, and q is the number of queries.
    # Space: O(√n + q)
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        res = 0
        MOD = 10**9 + 7
        n = len(nums)
        T = int(n**0.5)  # T=√n

        groups = [[] for _ in range(T)]
        for q in range(len(queries)):
            l, r, k, v = queries[q]
            if k < T:
                groups[k].append((l, r, v))
            else:
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % MOD

        dif = [1] * (n + T)
        for k in range(1, T):
            if not groups[k]:
                continue
            dif[:] = [1] * len(dif)
            for l, r, v in groups[k]:
                dif[l] = dif[l] * v % MOD
                R = ((r - l) // k + 1) * k + l
                dif[R] = dif[R] * pow(v, MOD - 2, MOD) % MOD

            for i in range(k, n):
                dif[i] = dif[i] * dif[i - k] % MOD
            for i in range(n):
                nums[i] = nums[i] * dif[i] % MOD

        for i in range(len(nums)):
            res ^= nums[i]

        return res
