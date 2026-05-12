class Solution:
    # Date Solved: 11 May 2026, Monday, Daily Problem
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda task: task[1] - task[0])
        min_energy_needed = 0
        for actual, minimum in tasks:
            # Either we have enough energy carried over (just add this task's cost) or we don't have enough to even start, so we must have at least `minimum`
            min_energy_needed = max(min_energy_needed + actual, minimum)
        return min_energy_needed
