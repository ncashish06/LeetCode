class Solution:
    # Date Solved: 13 July 2026, Monday, POTD
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # Approach 1 - Using simple BFS
        # Time: O(N), where N is the number of valid sequential digits in the range
        # Space: O(N), where N is the number of valid sequential digits in the range (queue size)
        queue = deque(range(1, 9))  # digits 1 through 8
        result = []

        while queue:
            temp = queue.popleft()

            if low <= temp <= high:
                result.append(temp)

            last_digit = temp % 10
            if last_digit + 1 <= 9:
                queue.append(temp * 10 + (last_digit + 1))

        return result
        """
        # Approach 2 - Using workaround (precomputed list)
        # Time: O(1)
        # Space: O(1)
        all_possible = [
            12,
            23,
            34,
            45,
            56,
            67,
            78,
            89,
            123,
            234,
            345,
            456,
            567,
            678,
            789,
            1234,
            2345,
            3456,
            4567,
            5678,
            6789,
            12345,
            23456,
            34567,
            45678,
            56789,
            123456,
            234567,
            345678,
            456789,
            1234567,
            2345678,
            3456789,
            12345678,
            23456789,
            123456789,
        ]

        result = []
        for num in all_possible:
            if num < low:
                continue
            if num > high:
                break
            result.append(num)

        return result
        """
