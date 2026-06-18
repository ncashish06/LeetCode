class Solution:
    # Date Solved: 18 June 2026, Thursday, POTD
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = 6 * minutes
        hour_angle = 30 * hour + 0.5 * minutes
        res = abs(hour_angle - minute_angle)
        return res if res <= 180 else 360 - res
