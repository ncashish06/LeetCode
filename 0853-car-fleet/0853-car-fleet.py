class Solution:
    # Date Solved: 26 July 2026, Sunday
    # NC150
    # Refer: NeetCode. In NeetCode's video, question mentions that it is single lane and overtaking is not possible.
    # No need of stack (like used by many YouTube solutions), just a single variable would suffice.
    """
    For visualization, think of each car's position on a Position vs. Time graph based on speed, and see if the lines intersect before/at the target.
    For code:
    1) Start from the last position (nearest to target) because if you start from the beginning, you don't know the final speed of the car, as they may slow down to match the slowest speed in the fleet ahead.
    2) For each car, calculate when it would arrive at the target if nothing were in its way (solo time).
    3) Compare this car's solo time to the time of the fleet currently ahead (prev_time):
    - If this car's time is later than prev_time, it's too slow to catch up — it forms a new fleet, and its time becomes the new prev_time.
    - If this car's time is at or before prev_time, it catches up to the fleet ahead and merges with it, traveling at that fleet's (slower) speed. prev_time stays unchanged.
    """

    # Time: O(nlogn) for sorting, Space: O(n) for cars list
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        for i in range(n):
            cars.append((position[i], speed[i]))

        # Sort by position (closest to target first); pairing keeps each car's speed tied to its position
        cars.sort(reverse=True)

        fleets = 0
        prev_time = 0  # time taken by the fleet currently ahead to reach target

        # Go through each car, starting from the one closest to target
        for pos, spd in cars:
            # Time this car would take to reach target if nothing blocked it
            time = (target - pos) / spd

            # If this car is slower than the fleet ahead, it can't catch up
            # so it becomes its own new fleet
            if time > prev_time:
                fleets += 1
                prev_time = time
            # Otherwise, it catches up to the fleet ahead and joins it
            # (no change to prev_time needed)

        return fleets
