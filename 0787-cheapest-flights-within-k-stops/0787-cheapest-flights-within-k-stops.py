from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # O(E*K) where E is the number of flights (edges) and K is the maximum number of stops allowed.
         # Note that graph = [[]] * n won't work. You think you're making: [[], [], []], but this creates one list in memory and thencreates three references (pointers) to that exact same list.
        graph = [[] for _ in range(n)]
        for frm, to, price in flights:
            graph[frm].append([to, price]) # Only from, to because this is directed graph
        
        min_price = [float("inf")]*n
        min_price[src] = 0
        q = deque([[src, 0, 0]])

        while len(q):
            [curr_node, curr_price, stops] = q.popleft()
            if stops > k:
                continue
            for [neighbor, neighbor_price] in graph[curr_node]:
                new_price = curr_price + neighbor_price
                if new_price < min_price[neighbor]:
                    min_price[neighbor] = new_price
                    q.append([neighbor, new_price, stops+1])


        return -1 if min_price[dst] == float('inf') else min_price[dst]
        