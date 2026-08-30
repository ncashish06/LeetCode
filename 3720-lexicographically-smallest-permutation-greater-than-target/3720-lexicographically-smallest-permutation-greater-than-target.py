class Solution:
    # Date Solved: 27 August 2026, Thursday, POTD
    # Refer: codestorywithMIK
    # Approach: Greedy + backtracking
    # Time: O(n), Space: O(n)
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        self.result = ""

        def solve(curr, count, target, i, greater):
            if i == len(target):
                if greater:
                    self.result = "".join(curr)
                    return True
                return False

            for c in range(26):
                ch = chr(ord("a") + c)

                if count[c] == 0:
                    continue

                if not greater and ch < target[i]:
                    continue

                curr.append(ch)
                count[c] -= 1

                isGreater = greater or ch > target[i]

                if solve(curr, count, target, i + 1, isGreater):
                    return True

                curr.pop()
                count[c] += 1

            return False

        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord("a")] += 1

        curr = []
        solve(curr, count, target, 0, False)

        return self.result
