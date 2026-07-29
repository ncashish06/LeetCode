class Solution:
    # Date Solved: 29 July 2026, Wednesday, POTD
    # Refer: codestorywithMIK
    # Approach: Factorisation + Cumulative Sum + Binary Search
    # Time: O(n × 26 × 26 × logk)
    # Space: O(n) for additional string
    def nCr(self, n: int, r: int, k: int) -> int:
        # nCr == nC(n-r)
        # 5C3 == 5C2
        # 5C2 == 5C(5-2) = 5C3
        r = min(r, n - r)  # nCr == nC(n-r)

        result = 1

        for i in range(1, r + 1):  # O(log2(k))
            result = result * (n - r + i) // i  # result is becoming twice

            if result >= k:
                return k

        return result

    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)

        mid = " "
        if n % 2 == 1:  # odd length
            mid = s[n // 2]

        count = [0] * 26
        for i in range(n):
            if n % 2 == 1 and i == n // 2:
                continue  # mid character reserved for middle one
            count[ord(s[i]) - ord("a")] += 1

        # half frequency will be used to build halfResult
        for i in range(26):
            count[i] //= 2

        half_result = []
        half = n // 2

        for i in range(half):  # O(n/2)
            # I am trying to fill ith position
            # What if I could never fill a character in ith position
            placed_character = False  # in ith position
            for j in range(26):  # which character to put
                if count[j] > 0:
                    count[j] -= 1

                    # count number of ways
                    ways = 1
                    letters = 0
                    for c in range(26):
                        letters += count[c]

                    for c in range(26):
                        if count[c] > 0:
                            ways *= self.nCr(letters, count[c], k)  # log2(k)
                            letters -= count[c]

                        if ways >= k:
                            break

                    if ways >= k:  # this block contains my kth one
                        half_result.append(
                            chr(j + ord("a"))
                        )  # fixed this character at ith position
                        placed_character = True
                        break

                    k -= ways  # when k >= ways
                    count[j] += 1

            if not placed_character:
                return ""

        # halfResult + mid + (reverse of halfResult)
        rev = half_result[::-1]  # O(n/2)

        if mid != " ":
            half_result.append(mid)

        return "".join(half_result) + "".join(rev)
