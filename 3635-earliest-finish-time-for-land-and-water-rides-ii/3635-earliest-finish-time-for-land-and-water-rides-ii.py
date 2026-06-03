class Solution:
    # Date Solved: 3 June 2026, Wednesday
    def findFinish(self, startTime1, duration1, startTime2, duration2):
        n, m = len(startTime1), len(startTime2)
        finish1, finish2 = float("inf"), float("inf")
        for i in range(n):
            finish1 = min(finish1, startTime1[i] + duration1[i])

        for j in range(m):
            finish2 = min(max(finish1, startTime2[j]) + duration2[j], finish2)

        return finish2

    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        firstLand = self.findFinish(
            landStartTime, landDuration, waterStartTime, waterDuration
        )
        firstWater = self.findFinish(
            waterStartTime, waterDuration, landStartTime, landDuration
        )
        return min(firstLand, firstWater)
