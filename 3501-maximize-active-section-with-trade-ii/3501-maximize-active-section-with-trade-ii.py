class Solution:
    # Date Solved: 22 July 2026, Wednesday, POTD
    # Refer: codestorywithMIK
    # Time: O(n + q*log n), Space: O(n + q)
    def buildSegmentTree(self, i, l, r, segmentTree, arr):
        if l == r:
            segmentTree[i] = arr[l]
            return

        mid = l + (r - l) // 2
        self.buildSegmentTree(2 * i + 1, l, mid, segmentTree, arr)
        self.buildSegmentTree(2 * i + 2, mid + 1, r, segmentTree, arr)
        segmentTree[i] = max(segmentTree[2 * i + 1], segmentTree[2 * i + 2])

    def constructST(self, arr, n):
        segmentTree = [0] * (4 * n)
        self.buildSegmentTree(0, 0, n - 1, segmentTree, arr)
        return segmentTree

    def querySegmentTree(self, start, end, i, l, r, segmentTree):
        if l > end or r < start:
            return float("-inf")

        if l >= start and r <= end:
            return segmentTree[i]

        mid = l + (r - l) // 2
        return max(
            self.querySegmentTree(start, end, 2 * i + 1, l, mid, segmentTree),
            self.querySegmentTree(start, end, 2 * i + 2, mid + 1, r, segmentTree),
        )

    def RMQ(self, st, n, a, b):
        return self.querySegmentTree(a, b, 0, 0, n - 1, st)

    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
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

        # If there is only one block of zeros
        # example: s = "11000011", answer = simply count of 1s "activeCount"
        if m < 2:
            return [activeCount] * len(queries)

        blockSize = [blockEnd[k] - blockStart[k] + 1 for k in range(m)]

        # pairSum[i] = blockSize[i] + blockSize[i+1]
        N = m - 1  # this many pairs will be there in pairSum
        pairSum = [blockSize[k] + blockSize[k + 1] for k in range(N)]

        st = self.constructST(pairSum, N)

        result = []
        for l, r in queries:  # O(q * log n)
            # first block reaching into the window from the left
            low = bisect_left(blockEnd, l)
            # last block reaching into the window from the right
            high = bisect_right(blockStart, r) - 1

            maxPairSum = 0
            if low < high:  # need at least two blocks in the window
                firstLen = blockEnd[low] - max(blockStart[low], l) + 1
                lastLen = min(blockEnd[high], r) - blockStart[high] + 1

                if high - low == 1:  # exactly two blocks only
                    maxPairSum = firstLen + lastLen
                else:
                    pair1 = firstLen + blockSize[low + 1]
                    pair2 = blockSize[high - 1] + lastLen
                    rmqMaxPairSum = (
                        self.RMQ(st, N, low + 1, high - 2) if low + 1 <= high - 2 else 0
                    )
                    maxPairSum = max(pair1, pair2, rmqMaxPairSum)

            result.append(maxPairSum + activeCount)

        return result
