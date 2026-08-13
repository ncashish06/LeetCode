class Solution:
    # Date Solved: 13 August 2026, Thursday, POTD
    # Refer: codestorywithMIK
    # Approach: Segment Tree
    # Time: O(n + klogn), build: O(n) and each update: O(log n), done k times -> O(klogn)
    # Space: O(4*n) ~ O(n)
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)  # mutable for updates
        segTree = [None] * (4 * n)  # segment tree size 4*n

        def merge(L, R, leftLen, rightLen):
            res = {}
            res["leftChar"] = L["leftChar"]
            res["rightChar"] = R["rightChar"]

            res["pre"] = L["pre"]
            if L["pre"] == leftLen and L["rightChar"] == R["leftChar"]:
                res["pre"] = L["pre"] + R["pre"]

            res["suf"] = R["suf"]
            if R["suf"] == rightLen and L["rightChar"] == R["leftChar"]:
                res["suf"] = R["suf"] + L["suf"]

            res["maxLen"] = max(L["maxLen"], R["maxLen"])
            if L["rightChar"] == R["leftChar"]:
                res["maxLen"] = max(res["maxLen"], L["suf"] + R["pre"])

            return res

        def buildSegmentTree(i, l, r):
            if l == r:
                segTree[i] = {
                    "pre": 1,
                    "suf": 1,
                    "maxLen": 1,
                    "leftChar": s[l],
                    "rightChar": s[l],
                }
                return
            mid = l + (r - l) // 2
            buildSegmentTree(2 * i + 1, l, mid)
            buildSegmentTree(2 * i + 2, mid + 1, r)
            segTree[i] = merge(
                segTree[2 * i + 1], segTree[2 * i + 2], mid - l + 1, r - mid
            )

        def update(i, l, r, pos, ch):
            if l == r:  # l == r == pos
                segTree[i] = {
                    "pre": 1,
                    "suf": 1,
                    "maxLen": 1,
                    "leftChar": ch,
                    "rightChar": ch,
                }
                return
            mid = l + (r - l) // 2
            if pos <= mid:
                update(2 * i + 1, l, mid, pos, ch)
            else:
                update(2 * i + 2, mid + 1, r, pos, ch)
            segTree[i] = merge(
                segTree[2 * i + 1], segTree[2 * i + 2], mid - l + 1, r - mid
            )

        buildSegmentTree(0, 0, n - 1)

        k = len(queryIndices)
        result = [0] * k

        for idx in range(k):
            pos = queryIndices[idx]
            ch = queryCharacters[idx]
            update(0, 0, n - 1, pos, ch)
            result[idx] = segTree[0]["maxLen"]  # root node covers entire string

        return result
