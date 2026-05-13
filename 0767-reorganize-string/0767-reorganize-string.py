class Solution:
    # Date Solved: 7 May 2026, Thursday
    # Got this question in Amazon Interview on 2 April 2026, Thursday
    # This question is asked a lot in Big Tech companies.
    # Refer: Part of NeetCode 250 solution
    """
    Similarity to LC358 (Rearrange String k Distance Apart):
        - LC767 is LC358 with k=2 (same character must be at least 2 apart, i.e. no adjacency)
        - Approach 1 (heap + prev) is literally LC358 with a cooldown queue of size 1
        - In LC358, prev becomes a deque of size k; here k=2 so a single prev slot suffices
        - Approaches 2 & 3 are LC767-specific optimizations exploiting the fixed 26-char alphabet
          and the simpler k=2 constraint; they do not generalize to arbitrary k
    """
    import heapq

    def reorganizeString(self, s: str) -> str:
        # Best Approach: Refer: Youtube codestorywithMIK
        # Time: O(n + k log k) where k = unique characters (at most 26). Since k is bounded by 26 (constant), this simplifies to O(n) in practice.
        n = len(s)
        count = [0] * 26

        # O(n) - iterating through string
        for ch in s:
            count[ord(ch) - ord("a")] += 1
            # Return if frequency of any character is greater than n/2
            if count[ord(ch) - ord("a")] > (n + 1) // 2:
                return ""

        pq = []  # Space: O(k) for heap, at most 26 unique chars

        # O(k log k) - building the heap, iterating through 26 characters (constant, but let's call it k unique chars)
        for i in range(26):
            if count[i] > 0:
                heapq.heappush(pq, (-count[i], chr(i + ord("a"))))

        result = []

        # O(k log k) - the while loop runs O(k) times, each pop/push is O(log k)
        while len(pq) >= 2:
            cnt1, ch1 = heapq.heappop(pq)
            cnt2, ch2 = heapq.heappop(pq)

            result.append(ch1)
            result.append(ch2)

            if cnt1 + 1 < 0:
                heapq.heappush(pq, (cnt1 + 1, ch1))

            if cnt2 + 1 < 0:
                heapq.heappush(pq, (cnt2 + 1, ch2))

        """
        When the input has an odd length, and the most frequent character has one leftover
        s = "aab"  -> result = "ab" from loop, then "a" appended -> "aba"
        s = "aabb" -> result = "abab" from loop, nothing left, below if is false
        s = "a"    -> loop never runs, "a" appended directly 
        """
        if pq:
            result.append(pq[0][1])

        return "".join(result)

        """
        # Approach 1: Frequency Count and Max Heap
        # Time: O(n log k) and Auxiliary Space: O(k) — heap and Counter store at most k unique characters
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""  # Most frequent char stuck with no valid neighbor

            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1  # Increment since counts are stored as negatives

            if prev:
                heapq.heappush(maxHeap, prev)  # Re-add previous char now that it's safe
                prev = None

            if cnt != 0:
                prev = [
                    cnt,
                    char,
                ]  # Hold out current char so it isn't picked consecutively

        return res
        
        # Approach 2: Frequency Count and Odd/Even Indices
        # Time: O(n) and Auxiliary Space: O(1) — freq array is always fixed at 26 elements
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord("a")] += 1

        max_idx = freq.index(max(freq))
        max_freq = freq[max_idx]
        if max_freq > (len(s) + 1) // 2:
            return ""

        res = [""] * len(s)
        idx = 0
        max_char = chr(max_idx + ord("a"))

        # Fill even indices with the most frequent character first
        while freq[max_idx] > 0:
            res[idx] = max_char
            idx += 2
            freq[max_idx] -= 1

        # Fill remaining characters in any order across remaining slots
        for i in range(26):
            while freq[i] > 0:
                if idx >= len(s):  # Even slots exhausted, wrap to odd indices
                    idx = 1
                res[idx] = chr(i + ord("a"))
                idx += 2
                freq[i] -= 1

        return "".join(res)

        # Approach 3: Frequency Count — Greedy Top Two
        # Time: O(n) and Auxiliary Space: O(1) — freq array is always fixed at 26 elements
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord("a")] += 1

        max_freq = max(freq)
        if max_freq > (len(s) + 1) // 2:
            return ""

        res = []
        while len(res) < len(s):
            # Pick and place the most frequent character
            maxIdx = freq.index(max(freq))
            char = chr(maxIdx + ord("a"))
            res.append(char)
            freq[maxIdx] -= 1

            if freq[maxIdx] == 0:
                continue  # No need to find second char if first is now exhausted

            # Temporarily exclude the first character to find the next most frequent
            tmp = freq[maxIdx]
            freq[maxIdx] = float("-inf")
            nextMaxIdx = freq.index(max(freq))
            char = chr(nextMaxIdx + ord("a"))
            res.append(char)
            freq[maxIdx] = tmp  # Restore the first character's count
            freq[nextMaxIdx] -= 1

        return "".join(res)
        """
