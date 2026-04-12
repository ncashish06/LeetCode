import math


class Solution:
    # Weekly Contest 497
    # Date Solved: 11 April 2026, Saturday
    def internalAngles(self, sides: list[int]) -> list[float]:
        sides.sort()
        a, b, c = sides[0], sides[1], sides[2]

        if a + b <= c:  # sum of 2 sides must be greater than the third side
            return []

        """
        Law of Cosines to find the internal angles. 
        For sides a, b, and c, the angle C (opposite side c) is calculated as:
        cos(C) = {a^2 + b^2 - c^2}/{2ab}
        C = arccos({a^2 + b^2 - c^2}/{2ab})
        Convert from radians to degrees.
        """

        def get_angle(s1, s2, opp):
            cos_val = (s1**2 + s2**2 - opp**2) / (2 * s1 * s2)
            return math.degrees(math.acos(cos_val))

        angle_A = get_angle(b, c, a)
        angle_B = get_angle(a, c, b)
        angle_C = get_angle(a, b, c)

        return sorted([angle_A, angle_B, angle_C])
