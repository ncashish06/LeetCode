class Solution:
    # Date Solved: 31 May 2026, Sunday, POTD
    # Time: O(nlogn)
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for i in range(len(asteroids)):
            if mass < asteroids[i]:
                return False
            mass += asteroids[i]
        return True
