class Solution:
    # Date Solved: 2 June 2026, Tuesday, POTD
    # Brute force
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        ans = float("inf")

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                # Option 1: land ride i first, then water ride j
                land_finish = landStartTime[i] + landDuration[i]
                water_start = max(land_finish, waterStartTime[j])
                water_finish = water_start + waterDuration[j]
                ans = min(ans, water_finish)

                # Option 2: water ride j first, then land ride i
                water_finish2 = waterStartTime[j] + waterDuration[j]
                land_start = max(water_finish2, landStartTime[i])
                land_finish2 = land_start + landDuration[i]
                ans = min(ans, land_finish2)

        return ans
