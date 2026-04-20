class Solution:
    # Date Solved: 20 April 2026, Monday
    # This problem can also be solved with DFS using stack instead of queue
    # "Height" or "Diameter" problems usually give you a TreeNode object (with .left and .right pointers). Here, the tree is "flat". It's hidden inside two arrays.
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
