class Solution:
    # Date Solved: 20 May 2026, Wednesday
    # POTD
    # Time: O(m.d + n.d) where m = length of arr1, n = length of arr2, d = max number of digits in any number (at most 10 for 32-bit integers), so effectively: O(m + n)
    # Space: O(m.d), the prefix_set stores at most d prefixes per number in arr1, so it holds at most m·d entries. Again since d <= 10, this is effectively O(m).
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Store all prefixes of every number in arr1, e.g. 1000 -> adds 1000, 100, 10, 1
        prefix_set = set()
        for n in arr1:
            while n and n not in prefix_set:
                prefix_set.add(n)
                n = n // 10

        res = 0
        for n in arr2:
            # Chop digits from the right until we find a match in prefix_set, e.g. 1000 -> try 1000, 100, 10, 1
            while n and n not in prefix_set:
                n = n // 10

            # If n > 0, we found a common prefix — check if it's the longest
            if n:
                res = max(res, len(str(n)))

        return res
