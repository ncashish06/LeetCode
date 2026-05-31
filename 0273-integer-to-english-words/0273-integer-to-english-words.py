class Solution:
    # Date Solved: 31 May 2026, Sunday
    # Reference: NeetCode YouTube
    # This question was asked in one of the technical rounds of an Amazon India SDE2 interview, as shared by an interviewee on LeetCode Discuss.
    # Time: O(1) — input is bounded by 2^31-1, so there are at most 4 chunks of 3 digits, each requiring a fixed amount of work.
    # Space: O(1) — lookup tables and result list are all fixed size.
    def numberToWords(self, num: int) -> str:
        # Core idea: split the number into groups of 3 digits from right to left,
        # convert each group to words, then attach the appropriate scale label (Thousand, Million, Billion).
        # e.g. 1,234,567 -> [1] Million + [234] Thousand + [567]
        if num == 0:
            return "Zero"

        ones_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        tens_map = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }

        def get_string(n):
            # Converts a number in range [1, 999] to its English word representation.
            res = []

            hundreds = n // 100
            if hundreds:
                # e.g. n=347: hundreds=3 -> "Three Hundred"
                # Note: hundreds=0 is falsy, so chunks like 043 correctly skip this step.
                res.append(ones_map[hundreds] + " Hundred")

            last_2 = n % 100
            if last_2 >= 20:
                # e.g. last_2=47: tens=4, ones=7 -> "Forty" + "Seven"
                tens, ones = last_2 // 10, last_2 % 10
                res.append(tens_map[tens * 10])
                if ones:
                    # e.g. last_2=40: ones=0 -> skip, giving just "Forty" with no trailing word
                    res.append(ones_map[ones])
            elif last_2:
                # Handles 1–19 directly via ones_map (e.g. last_2=13 -> "Thirteen").
                # Also handles cases like n=102 where last_2=02=2 (integer, not string) -> "Two".
                res.append(ones_map[last_2])
            # last_2=0 is falsy, so n=100 correctly gives just "One Hundred" with nothing appended after.

            return " ".join(res)

        postfix = ["", " Thousand", " Million", " Billion"]
        i = 0
        res = []

        while num:
            digits = num % 1000  # extract the rightmost 3-digit chunk
            s = get_string(digits)
            if s:
                # Skip empty chunks — e.g. 1,000,000,643 has a middle chunk of 000,
                # which get_string returns "" for, so we avoid "Six Hundred Forty Three  Billion".
                res.append(s + postfix[i])
            num = num // 1000  # shift right by 3 digits to process the next chunk
            i += 1

        # Chunks were collected right-to-left, so reverse to get the correct order.
        # e.g. ["Six Hundred Forty Three", "One Billion"] -> ["One Billion", "Six Hundred Forty Three"]
        res.reverse()
        return " ".join(res)
