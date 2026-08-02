class Solution:
    # Date Solved: 1 August 2026, Saturday, POTD
    # Refer: codestorywithMIK
    # Game Strategy: When it is your turn, do your best and choose maximum. Since opponent also plays optimally, expect the worst from result after opponent's turn. So it is alternating max->min->max->min... structure of the recursion, i.e., classic minimax: maximize on your turn, minimize (from your perspective) on the opponent's turn
    def predictTheWinner(self, nums: List[int]) -> bool:
        # Approach: Recursion + Memo - I
        # Time: O(n^2) with memo else O(2^n)
        # Space: O(n^2) with memo else O(2^n)
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
