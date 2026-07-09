class Solution:
    # Date Solved: 9 July 2026, Thursday, POTD
    # Refer: Claude. Union-find approach is overkill here.
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        # Assign each index a group id; new group starts whenever the gap to the previous element exceeds maxDiff
        group = [0] * n
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                group[i] = group[i - 1] + 1
            else:
                group[i] = group[i - 1]

        # Two nodes are connected iff they belong to the same group
        return [group[u] == group[v] for u, v in queries]
