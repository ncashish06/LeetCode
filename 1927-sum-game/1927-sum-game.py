class Solution:
    # Date Solved: 23 August 2026, Sunday, POTD
    # Refer: codestorywithMIK
    # Time: O(n), Space: O(1)
    def sumGame(self, num: str) -> bool:
        n = len(num)
        leftKnownSum = 0
        rightKnownSum = 0

        leftQnMarkCount = 0
        rightQnMarkCount = 0

        for i in range(n):
            if num[i] == "?":
                if i < n // 2:
                    leftQnMarkCount += 1
                else:
                    rightQnMarkCount += 1
            else:
                if i < n // 2:
                    leftKnownSum += int(num[i])
                else:
                    rightKnownSum += int(num[i])

        totalQnMarks = leftQnMarkCount + rightQnMarkCount
        if totalQnMarks % 2 == 1:  # Odd - Alice always wins
            return True

        LEFT = 2 * leftKnownSum + 9 * leftQnMarkCount
        RIGHT = 2 * rightKnownSum + 9 * rightQnMarkCount

        if LEFT == RIGHT:  # Bob wins
            return False

        return True
