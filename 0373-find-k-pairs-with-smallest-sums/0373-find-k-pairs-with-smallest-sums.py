import heapq


class Solution:
    # Date Solved: 10 June 2026, Wednesday
    # Refer: codestorywithMIK
    # Time: O(K*logK), O(K) for while loop and O(logK) for heap operations
    # Space: O(K)
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        m, n = len(nums1), len(nums2)

        # Min-heap: (sum, i, j)
        min_heap = [(nums1[0] + nums2[0], 0, 0)]
        visited = {(0, 0)}
        result = []

        while k and min_heap:
            total, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            k -= 1

            # Push (i, j+1) if not visited
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

            # Push (i+1, j) if not visited
            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

        return result
