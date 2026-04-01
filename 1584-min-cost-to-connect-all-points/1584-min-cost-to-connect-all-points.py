class Solution:
    import heapq

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_points = len(points)
        total_mst_cost = 0
        nodes_in_mst = 0
        visited = [False] * num_points

        # PQ stores [distance_to_reach_node, node_index]
        min_heap = [[0, 0]]

        while nodes_in_mst < num_points:
            edge_weight, curr_node = heapq.heappop(min_heap)

            if visited[curr_node]:
                continue

            visited[curr_node] = True
            total_mst_cost += edge_weight
            nodes_in_mst += 1

            curr_x, curr_y = points[curr_node]

            for next_node in range(
                num_points
            ):  # try to find min cost path from each point to all other points
                if not visited[next_node]:
                    next_x, next_y = points[next_node]
                    manhattan_dist = abs(curr_x - next_x) + abs(curr_y - next_y)
                    heapq.heappush(min_heap, (manhattan_dist, next_node))

        return total_mst_cost
