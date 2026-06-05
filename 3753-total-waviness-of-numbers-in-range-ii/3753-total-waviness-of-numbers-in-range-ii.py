class Solution:
    # Date Solved: 5 June 2026, Friday, POTD
    # Time : O(n * 10 * 10 * 10) where n = number of digits ~ O(1) since n <= 15
    # Space: O(n * 10 * 10) for memoization
    # Refer: codestorywithMIK
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(s, n, curr, prev_prev, prev, is_limited, is_leading_zero, memo):
            if curr == n:
                return (1, 0)

            key = (curr, prev_prev, prev)
            if not is_limited and not is_leading_zero and prev_prev >= 0 and prev >= 0:
                if key in memo:
                    return memo[key]

            total_numbers = 0
            total_wave_score = 0
            limit_digit = int(s[curr]) if is_limited else 9

            for digit in range(0, limit_digit + 1):
                new_is_leading_zero = is_leading_zero and (digit == 0)
                new_prev_prev = prev
                new_prev = -1 if new_is_leading_zero else digit

                rem_numbers, rem_wave_score = solve(
                    s,
                    n,
                    curr + 1,
                    new_prev_prev,
                    new_prev,
                    is_limited and (digit == limit_digit),
                    new_is_leading_zero,
                    memo,
                )

                if not new_is_leading_zero and prev_prev >= 0 and prev >= 0:
                    is_peak = prev_prev < prev and prev > digit
                    is_valley = prev_prev > prev and prev < digit
                    if is_peak or is_valley:
                        total_wave_score += rem_numbers

                total_numbers += rem_numbers
                total_wave_score += rem_wave_score

            if not is_limited and not is_leading_zero and prev_prev >= 0 and prev >= 0:
                memo[key] = (total_numbers, total_wave_score)

            return (total_numbers, total_wave_score)

        def func(num):
            if num < 100:
                return 0
            s = str(num)
            n = len(s)
            memo = {}
            _, total_wave_score = solve(s, n, 0, -1, -1, True, True, memo)
            return total_wave_score

        return func(num2) - func(num1 - 1)
