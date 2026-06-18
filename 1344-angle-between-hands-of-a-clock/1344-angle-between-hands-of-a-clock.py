class Solution:
    # Date Solved: 18 June 2026, Thursday, POTD
    # Time: O(1), Space: O(1)
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = 6 * minutes              # minute hand: 360/60 = 6 deg/min
        hour_angle = 30 * hour + 0.5 * minutes  # hour hand: 360/12=30 deg/hr, plus drift of 0.5 deg/min
        res = abs(hour_angle - minute_angle)    # raw angle diff, can be up to 360
        return res if res <= 180 else 360 - res # take the smaller of the two possible angles
