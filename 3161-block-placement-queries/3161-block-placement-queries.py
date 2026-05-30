from sortedcontainers import SortedList


class Solution:
    # POTD, 30 May 2026. Saturday
    # Used Claude since segment tree not important for interviews
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        MAX_X = 50002
        size = 1
        while size < MAX_X:
            size <<= 1
        tree = [0] * (2 * size)

        def update(pos, val):
            i = pos + size
            tree[i] = val
            i >>= 1
            while i >= 1:
                tree[i] = max(tree[2 * i], tree[2 * i + 1])
                i >>= 1

        def query(l, r):  # max in [l, r]
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
        update(0, 0)

        results = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = sl.bisect_left(x)
                prev = sl[idx - 1]
                if idx < len(sl):
                    nxt = sl[idx]
                    update(nxt, nxt - x)  # shrink nxt's gap
                update(x, x - prev)
                sl.add(x)
            else:
                x, sz = q[1], q[2]
                idx = sl.bisect_right(x) - 1
                last = sl[idx]  # last obstacle <= x
                # Max gap among [obstacle→obstacle] pairs with right endpoint ≤ x
                seg_max = query(0, last)
                # Gap from last obstacle to x
                right_gap = x - last
                results.append(max(seg_max, right_gap) >= sz)

        return results
