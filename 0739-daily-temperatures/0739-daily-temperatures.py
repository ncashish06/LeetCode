class Solution:
    # Date Solved: 24 July 2026, Friday
    # NC150
    # Refer: NeetCode and Hello Interview. codestorywithMIK and Namaste DSA solve in reverse order which is not very intuitive during interviews.
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        # Approach-1: Brute Force
        # Time: O(n^2), Space: O(1)
        n = len(temperatures)
        days_to_wait = [0] * n

        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    days_to_wait[i] = j - i
                    break  # found nearest warmer day, stop scanning

        return days_to_wait
        """
        # Approach-2: Monotonic Stack
        # Whenever a problem asks for "next or previous warmer/greater/smaller" element, think monotonic stack — it avoids the repeated re-scanning of brute force.
        # Time: O(n) (not O(n^2) as each index is pushed and popped from the stack at most once)
        # Space: O(n)
        n = len(temperatures)
        days_to_wait = [0] * n
        stack = []  # stores indices of days waiting for a warmer day

        for curr_day in range(n):
            # pop all days that are colder than today -> today is their answer
            while stack and temperatures[curr_day] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                days_to_wait[prev_day] = curr_day - prev_day
            stack.append(curr_day)

        return days_to_wait
