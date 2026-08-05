class Solution:
    # Date Solved: 5 August 2026, Wednesday, POTD
    # Refer: codestorywithMIK
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        suspicious = [False] * n

        for u, v in invocations:
            adj[u].append(v)
            in_degree[v] += 1

        # BFS from k to mark all suspicious methods
        queue = deque([k])
        suspicious[k] = True

        while queue:
            curr = queue.popleft()
            for ngbr in adj[curr]:
                in_degree[ngbr] -= 1  # remove edges from within suspicious group
                if not suspicious[ngbr]:
                    queue.append(ngbr)
                    suspicious[ngbr] = True

        result = []
        cannot_remove = False

        # single suspicious group (all reachable from k) -> all-or-nothing removal
        for i in range(n):
            if suspicious[i] and in_degree[i] > 0:
                # in_degree[i] > 0 here = still called from OUTSIDE the group -> can't remove group, stop
                cannot_remove = True
                break
            if not suspicious[i]:
                result.append(i)

        if cannot_remove:
            return list(range(n))

        return result
