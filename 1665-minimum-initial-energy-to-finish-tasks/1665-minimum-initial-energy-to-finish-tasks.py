class Solution:
    # Date Solved: 11 May 2026, Monday, Daily Problem
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        """
        Greedy approach: sort tasks by (minimum - actual) ascending.
        For each task, (minimum - actual) represents the "buffer" it demands from your initial energy beyond what it actually costs.
        Tasks with a small buffer are  efficient as they don't require much cushion, so do them first while energy is high.
        Tasks with a large buffer are done last, where the accumulated starting energy can absorb that cushion without inflating the overall minimum.

        Time: O(nlogn), Space: O(logn) due to Python's Timsort (Merge sort recursion)
        """
        tasks.sort(key=lambda task: task[1] - task[0])
        min_energy_needed = 0
        for actual, minimum in tasks:
            # Either we have enough energy carried over (just add this task's cost) or we don't have enough to even start, so we must have at least `minimum`
            min_energy_needed = max(min_energy_needed + actual, minimum)
        return min_energy_needed
