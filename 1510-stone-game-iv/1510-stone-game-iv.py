class Solution:
    # Date Solved: 10 August 2026, Monday, POTD
    # Refer: codestorywithMIK
    def winnerSquareGame(self, n: int) -> bool:
        """
        # Approach-1: Recursion + Memoization
        # Time: O(n*sqrt(n)), Space: O(n)
        t = [-1] * (n + 1)

        def solve(n: int) -> bool:
            if n == 0:
                return False
            if t[n] != -1:
                return True if t[n] == 1 else False
            k = 1
            while k * k <= n:  # Time: O(sqrt(n))
                # Call for Bob, if False - Bob lost it, Alice won the game
                if solve(n - (k * k)) == False:
                    t[n] = 1
                    return True
                k += 1

            t[n] = 0  # Alice could never win. Lost it.
            return False

        # Alice k lie call hai ye. If it's true, Alice wins, else Alice looses
        return solve(n)
        """
        # Approach-2: Bottom Up
        # Time: O(n*sqrt(n)), Space: O(n)
        t = [False] * (n + 1)

        # Base case . n== 0, return false
        # i == 0
        t[0] = False  # base case

        i = 1
        while i < n + 1:
            k = 1
            while k * k <= i:
                if t[i - (k * k)] == False:
                    t[i] = True
                    break
                k += 1
            i += 1

        return t[n]  # return solve(n)
