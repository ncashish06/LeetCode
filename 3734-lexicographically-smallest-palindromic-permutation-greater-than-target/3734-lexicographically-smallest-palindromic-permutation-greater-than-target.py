class Solution:
    # Date Solved: 28 August 2026, Friday, POTD
    # Refer: codestorywithMIK
    # Approach: Greedy + backtracking
    # Time: O(26*n) ~ O(n), Space: O(n)
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        self.result = ""
        self.midChar = "$"
        self.half = 0

        def solve(curr, count, target, i, greater):
            if i == self.half:
                leftHalf = "".join(curr)
                rightHalf = leftHalf[::-1]

                candidate = leftHalf
                if self.midChar != "$":
                    candidate += self.midChar
                candidate += rightHalf

                if candidate > target:
                    self.result = candidate
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

        n = len(s)
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord("a")] += 1

        oddCount = 0
        for c in range(26):
            if count[c] % 2 == 1:
                oddCount += 1
                self.midChar = chr(c + ord("a"))

        if oddCount > 1:
            return ""

        halfCount = [cnt // 2 for cnt in count]
        self.half = n // 2

        curr = []
        solve(curr, halfCount, target, 0, False)
        return self.result
