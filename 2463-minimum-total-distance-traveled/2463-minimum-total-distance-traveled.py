class Solution:
    # Date Solved: 13 April 2026, Monday
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])

        factory_positions = []
        for pos, limit in factory:
            factory_positions.extend([pos] * limit)

        robot_count = len(robot)
        factory_count = len(factory_positions)
        # Memoization
        dp = [[None] * (factory_count + 1) for _ in range(robot_count + 1)]

        def calculate_min_distance(robot_idx, factory_idx):
            if dp[robot_idx][factory_idx] is not None:
                return dp[robot_idx][factory_idx]

            if robot_idx == robot_count:
                return 0
            if factory_idx == factory_count:
                return float("inf")

            # Option 1: Assign robot to this factory position
            assign = abs(
                robot[robot_idx] - factory_positions[factory_idx]
            ) + calculate_min_distance(robot_idx + 1, factory_idx + 1)

            # Option 2: Skip this factory position for the current robot
            skip = calculate_min_distance(robot_idx, factory_idx + 1)

            dp[robot_idx][factory_idx] = min(assign, skip)
            return dp[robot_idx][factory_idx]

        return calculate_min_distance(0, 0)
