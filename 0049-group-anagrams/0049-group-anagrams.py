class Solution:
    # Date Solved: 25 April 2026, Saturday
    # Refer: Neetcode 150 Course on freeCodeCamp.org YouTube
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}  # res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key not in res:  # can be avoided if you use res = defaultdict(list)
                res[tuple(count)] = []
            res[tuple(count)].append(s)
        return list(res.values())
