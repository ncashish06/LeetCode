class Solution:
    # Date Solved: 7 May 2026, Thursday
    # Got this question in Amazon Interview on 2 April 2026, Thursday
    # This question is asked a lot in Big Tech companies. This is a variation of LC621. Task Scheduler
    import heapq
    def reorganizeString(self, s: str) -> str:
        """
        # Standard solution with Max heap
        # Time: O(nlogk) where n is the length of string and k is the number of elements in the heap. The log k is the time to heapify. While accessing the top element is  constant time O(1), removing it (heappop) takes logarithmic time O(log n) because the data structure must be reshuffled to remain a valid heap.
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return res
        """
        # Namaste DSA solution: Even/Odd indices for max freq element approach
        freq = {}
        maxFreq = 0

        # Count frequency
        for c in s:
            freq[c] = freq.get(c, 0) + 1
            maxFreq = max(maxFreq, freq[c])
        
        n = len(s)
        # Impossible case
        if maxFreq > (n + 1) // 2:
            return ""

        # Sort characters by frequency (descending)
        chars = sorted(freq.keys(), key=lambda x: -freq[x])

        result = [""] * n
        i = 0
        # Fill even indices first, then odd
        for ch in chars:
            count = freq[ch]
            while count > 0:
                if i >= n:
                    i = 1
                result[i] = ch
                i += 2
                count -= 1
        return "".join(result)
