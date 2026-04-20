class Solution:
    # Date Solved: 20 April 2026, Monday
    # This problem can also be solved with DFS using stack instead of queue
    from collections import deque

    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        children_map = {}
        for i in range(len(pid)):
            parent = ppid[i]
            child = pid[i]

            if parent not in children_map:
                children_map[parent] = []
            children_map[parent].append(child)

        result = []
        queue = deque([kill])

        while queue:
            current = queue.popleft()
            result.append(current)

            if current in children_map:
                queue.extend(children_map[current])

        return result
