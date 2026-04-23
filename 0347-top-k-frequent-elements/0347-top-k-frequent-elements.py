import heapq
from collections import Counter


class Solution:
    # Date Solved: 23 April 2026, Thursday
    # Refer: Namaste DSA.
    # Intuition: Store elements frequency in Hash Map. Then you can sort based on the values and return top K but this approach would take time of O(nlogn). If we use heap here, we can reduce time to O(nlogk).
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)  # Time: O(n)
        min_heap = []
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))  # Time: O(logk)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for freq, num in min_heap]
