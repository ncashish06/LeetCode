class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        days_to_wait = [0] * n
        # In any problem which says "next" warmer (or next greater, next fastest, next positive, etc.), think of stack data structure.
        # This stack stores indices of days that haven't found a warmer day yet
        stack = []
        stack.append(n - 1)
        for curr_day in range(n - 2, -1, -1):
            while stack:
                top = stack[-1]
                if temperatures[curr_day] >= temperatures[top]:
                    stack.pop()
                else:
                    days_to_wait[curr_day] = top - curr_day
                    break
            stack.append(curr_day)
        return days_to_wait
