class Solution:
    # Date Solved: 6 May 2026, Wednesday
    # Blind 75, 1st question in the series of Jump Game
    # Refer: Namaste DSA. Solution approach starts from Brute-Force: O(n^n) approach to
    # O(n^2) approach with memoization and then
    # O(n) approach with Greedy algorithm
    def canJump(self, nums: List[int]) -> bool:
        """
        # Approach 2: Memoization │ Time: O(n^2), Space: O(n)
        # At each index, try all jumps 1..nums[i]. Cache the result so each
        # index is solved only once -> cuts the brute force O(n^n) down to O(n^2)
        end = len(nums) - 1
        memo = [-1] * len(nums)  # all unvisited

        def dfs(start):
            if start == end:
                return True
            if memo[start] != -1:  # already solved -> reuse result
                return memo[start]

            ans = False
            for i in range(1, nums[start] + 1):
                # only recurse if the jump stays in bounds AND we haven't found a valid path yet
                if not ans and start + i <= end:
                    ans = ans or dfs(start + i)

            memo[start] = ans  # cache before returning
            return ans

        return dfs(0)

        # Approach 3a: Greedy (Namaste DSA) │ Time: O(n), Space: O(1)
        # Track the farthest index reachable so far. If we ever step onto an
        # index beyond farthest, there's a gap we can't cross so return False.
        # Otherwise, keep extending farthest greedily.
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:  # current index is unreachable -> stuck
                return False
            farthest = max(farthest, i + nums[i])  # extend reach from here
        return True
        """
        # Approach 3b: Greedy (NeetCode) │ Time: O(n), Space: O(1)
        # Instead of tracking farthest forward, move the goal_post backward.
        # If index i can reach the current goal, i becomes the new goal.
        # At the end, if goal_post shifted all the way back to 0, then return True.
        goal_post = len(nums) - 1  # start: must reach the last index
        for i in range(len(nums) - 2, -1, -1):  # scan right to left
            if i + nums[i] >= goal_post:
                goal_post = i  # i can reach goal -> i is new goal

        return goal_post == 0
