class Solution:
    # Date Solved: 7 August 2026, Friday, POTD
    # Refer: codestorywithMIK
    # Approach: Greedily fill digit by digit trying prefixes
    # Time: O(n * log(t)), Space: O(n)
    def freeSlotsFiller(self, required: int, length: int) -> str:
        digits = []

        for digit in range(9, 1, -1):
            while required % digit == 0:
                digits.append(str(digit))
                required //= digit

        while len(digits) < length:
            digits.append("1")

        digits.reverse()
        return "".join(digits)

    def smallestNumber(self, num: str, t: int) -> str:
        n = len(num)

        # Check primes 2, 3, 5, 7 — t must only be composed of these
        temp = t
        for primeFact in (2, 3, 5, 7):
            while temp % primeFact == 0:
                temp //= primeFact

        if temp != 1:  # other prime factors exist -> impossible
            return "-1"

        # remainingFactor[i] = factor of t still needed after taking first i digits of num
        remainingFactor = [t] * (n + 1)
        for i in range(n):
            digit = int(num[i])

            if digit == 0:
                break

            remainingFactor[i + 1] = remainingFactor[i] // gcd(
                remainingFactor[i], digit
            )

        if remainingFactor[n] == 1:  # the input itself already works
            return num

        zeroPos = num.find("0")
        zeroIdx = n - 1
        if zeroPos != -1:
            zeroIdx = zeroPos

        for i in range(zeroIdx, -1, -1):
            required = remainingFactor[i]
            freeSlots = n - 1 - i

            for digit in range(int(num[i]) + 1, 10):
                furtherRequired = required // gcd(required, digit)
                requiredNumber = self.freeSlotsFiller(furtherRequired, freeSlots)

                if len(requiredNumber) == freeSlots:
                    return num[:i] + str(digit) + requiredNumber

        return self.freeSlotsFiller(t, n + 1)  # e.g. num = "11", t = 2^15
