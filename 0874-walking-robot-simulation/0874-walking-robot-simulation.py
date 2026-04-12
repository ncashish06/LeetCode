class Solution:
    # Date Solved: 6 April 2026, Monday
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # North, East, South, West (clockwise)
        facing = 0
        max_dist_sq = 0
        """
        Set comprehension: #Hash set
        Convert to a set of tuples(immutable and hashable) for O(1) lookups; lists are mutable and unhashable, so we "freeze" them into tuples. A set works like a dictionary that only contains keys, allowing us to instantly check if a coordinate exists without searching the entire list.
        For an object to be "hashable," its value must stay the same for its entire lifetime so that its "hash code" (its digital fingerprint) never changes. If you put a list in a hash table and then changed one of its numbers, its hash code would change, and the hash table would "lose" it - it would be looking in the wrong bucket!
        """
        obstacle_set = {tuple(o) for o in obstacles}

        for cmd in commands:
            if cmd == -1:  # Turn clockwise
                facing = (facing + 1) % 4
            elif cmd == -2:  # Turn counter clockwise
                facing = (facing - 1) % 4 # -1%4 = 3
            else:
                dx, dy = directions[facing]
                for _ in range(cmd):  # for magnitude, if cmd=4 then check if any of the next steps leads to obstacle
                    next_x, next_y = x + dx, y + dy
                    if (next_x, next_y) in obstacle_set:
                        break
                    x, y = next_x, next_y

            max_dist_sq = max(max_dist_sq, x**2 + y**2)
        return max_dist_sq

# Time: O(m+n), m=length of commands and n=length of obstacles
# The algorithm initially iterates over the obstacles array and hashes each obstacle’s coordinates, taking O(n) time.
# Space: O(n)
