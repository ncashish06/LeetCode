from collections import deque
class Solution:
    # solution is number of unconnected components (think like islands) - 1
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        
        # Note that graph = [[]] * n won't work. You think you're making: [[], [], []], but this creates one list in memory and then creates three references (pointers) to that exact same list.

        graph = [[] for _ in range(n)]
        for frm, to in connections:
            graph[frm].append(to)
            graph[to].append(frm)

        no_of_unconnected_components = 0
        visited = [False]*n

        def bfs(src):
            q = deque([src])
            visited[src]=True
            while len(q):
                curr_node = q.popleft()
                for neighbor in graph[curr_node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append(neighbor)

        for i in range(n):
            if not visited[i]:
                no_of_unconnected_components+=1
                bfs(i)

        return no_of_unconnected_components-1

