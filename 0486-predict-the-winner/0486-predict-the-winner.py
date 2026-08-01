class Solution:
    # Date Solved: 1 August 2026, Saturday, POTD
    # Refer: codestorywithMIK
    def predictTheWinner(self, nums: List[int]) -> bool:
        """
        # Approach 1: Recursion + Memo - I
        # Time: O(n^2), Space: O(n^2)
        n = len(nums)
        memo = {}

        def solve(l: int, r: int) -> int:
            if l > r:
                return 0
            if l == r:
                return nums[l]
            if (l, r) in memo:
                return memo[(l, r)]

            take_left = nums[l] + min(solve(l + 2, r), solve(l + 1, r - 1))
            take_right = nums[r] + min(solve(l, r - 2), solve(l + 1, r - 1))

            memo[(l, r)] = max(take_left, take_right)
            return memo[(l, r)]

        total = sum(nums)
        player1 = solve(0, n - 1)
        player2 = total - player1

        return player1 >= player2
        """
        # Approach 2: Using diff of score between players
        # Recursion + Memo - II
        # Time: O(n^2), Space: O(n^2)
        n = len(nums)
        memo = {}

        def maxDiff(l: int, r: int) -> int:
            if l == r:
                return nums[l]
            if (l, r) in memo:
                return memo[(l, r)]

            take_left = nums[l] - maxDiff(l + 1, r)
            take_right = nums[r] - maxDiff(l, r - 1)

            memo[(l, r)] = max(take_left, take_right)
            return memo[(l, r)]

        return maxDiff(0, n - 1) >= 0
