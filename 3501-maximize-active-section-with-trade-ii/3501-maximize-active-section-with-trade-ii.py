class Solution:
    # Date Solved: 22 July 2026, Wednesday, POTD
    # Refer: codestorywithMIK
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        activeCount = s.count("1")

        blockStart = []
        blockEnd = []

        i = 0
        while i < n:
            if s[i] == "0":
                start = i
                while i < n and s[i] == "0":
                    i += 1
                blockStart.append(start)
                blockEnd.append(i - 1)
            else:
                i += 1

        m = len(blockStart)

        # If there is only one block of zeros (or none)
        # example: s = "11000011", answer = simply count of 1s (activeCount)
        if m < 2:
            return [activeCount] * len(queries)

        blockSize = [blockEnd[k] - blockStart[k] + 1 for k in range(m)]

        # pairSum[k] = blockSize[k] + blockSize[k+1]
        N = m - 1  # this many pairs will be there in pairSum
        pairSum = [blockSize[k] + blockSize[k + 1] for k in range(N)]

        # ---- Segment tree (max) over pairSum ----
        segTree = [0] * (4 * N)

        def build(node: int, l: int, r: int) -> None:
            if l == r:
                segTree[node] = pairSum[l]
                return
            mid = (l + r) // 2
            build(2 * node + 1, l, mid)
            build(2 * node + 2, mid + 1, r)
            segTree[node] = max(segTree[2 * node + 1], segTree[2 * node + 2])

        def query(start: int, end: int, node: int, l: int, r: int) -> int:
            if l > end or r < start:
                return float("-inf")
            if l >= start and r <= end:
                return segTree[node]
            mid = (l + r) // 2
            return max(
                query(start, end, 2 * node + 1, l, mid),
                query(start, end, 2 * node + 2, mid + 1, r),
            )

        def RMQ(a: int, b: int) -> int:
            return query(a, b, 0, 0, N - 1)

        build(0, 0, N - 1)

        result = []
        for l, r in queries:  # O(q * log n)
            # first block reaching into the window from the left
            low = bisect.bisect_left(blockEnd, l)
            # last block reaching into the window from the right
            high = bisect.bisect_right(blockStart, r) - 1

            maxPairSum = 0
            if low < high:  # need at least two blocks in the window
                firstLen = blockEnd[low] - max(blockStart[low], l) + 1
                lastLen = min(blockEnd[high], r) - blockStart[high] + 1

                if high - low == 1:  # exactly two blocks only
                    maxPairSum = firstLen + lastLen
                else:
                    pair1 = firstLen + blockSize[low + 1]
                    pair2 = blockSize[high - 1] + lastLen
                    rmqMaxPairSum = RMQ(low + 1, high - 2) if low + 1 <= high - 2 else 0
                    maxPairSum = max(pair1, pair2, rmqMaxPairSum)

            result.append(maxPairSum + activeCount)

        return result
