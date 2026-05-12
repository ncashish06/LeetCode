class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[1] - t[0], reverse=True)
        ans = 0
        spent = 0
        for actual, minimum in tasks:
            ans = max(ans, spent + minimum)
            spent += actual
        return ans
