from sortedcontainers import SortedList


class Solution:
    # POTD, 30 May 2026. Saturday
    # Refer: codestorywithMIK, claude
    # Time : O(Q * logN) where Q = number of queries, N = max coordinate (50000)
    # Space : O(N) for the segment tree and sorted list
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        MAX_X = 50001
        size = 1
        while size < MAX_X:
            size <<= 1

        tree = [0] * (
            2 * size
        )  # Iterative segment tree - much less memory than 4*N recursive

        def update(pos, val):
            i = pos + size
            tree[i] = val
            i >>= 1
            while i >= 1:
                tree[i] = max(tree[2 * i], tree[2 * i + 1])
                i >>= 1

        def query(l, r):  # max in [l, r] inclusive
            res = 0
            l += size
            r += size + 1
            while l < r:
                if l & 1:
                    res = max(res, tree[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res = max(res, tree[r])
                l >>= 1
                r >>= 1
            return res

        sl = SortedList([0])
        result = []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = sl.bisect_right(x)  # position after x
                nxt = sl[idx] if idx < len(sl) else -1
                pre = sl[idx - 1]  # last obstacle before x

                update(x, x - pre)
                if nxt != -1:
                    update(nxt, nxt - x)
                sl.add(x)
            else:
                x, sz = q[1], q[2]
                idx = sl.bisect_right(x) - 1  # last obstacle <= x
                pre = sl[idx]

                max_gap = query(0, pre)
                best = max(max_gap, x - pre)
                result.append(best >= sz)

        return result
