import heapq
from collections import defaultdict

class Solution:
    # Date Solved: 3 July 2026, Friday, POTD
    # Refer: codestorywithMIK,Dijkstra's + Binary Search on Answer
    # Whenever a problem says "Maximize the minimum" or "Minimize the maximum", it is Binary Search problem.
    # Time: O((E+V)log(V) * log(U)), E = number of edges, V = number of vertices, (E+V)log(V) is for Dijkstra and log(U) is for Binary Search, U = r-l
    # Space: O(V+E)
    def check(self, mid: int, n: int, k: int, adj: dict) -> bool:
        result = [float("inf")] * n
        result[0] = 0

        pq = [(0, 0)]  # (distance, node)

        while pq:
            d, node = heapq.heappop(pq)

            if d > k:
                return False

            if node == n - 1:
                return True

            if d > result[node]:
                continue

            for adjNode, edgeCost in adj[node]:
                if edgeCost < mid:  # because I want the score to be mid
                    continue

                if d + edgeCost < result[adjNode]:
                    result[adjNode] = d + edgeCost
                    heapq.heappush(pq, (d + edgeCost, adjNode))

        return False

    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = defaultdict(list)

        l, r = float("inf"), 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue

            adj[u].append((v, w))
            l = min(l, w)
            r = max(r, w)

        answer = -1

        while l <= r:
            mid = l + (r - l) // 2

            if self.check(mid, n, k, adj):
                answer = mid
                l = mid + 1
            else:
                r = mid - 1

        return answer
