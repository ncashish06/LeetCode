import heapq
from collections import Counter

class Solution:
    # Date Solved: 23 April 2026, Thursday
    # Refer: Namaste DSA.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        # Approach 1: The following approach using "min heap" works perfectly for interview and in fact the most common solution.
        # Intuition: Store elements frequency in Hash Map. Then you can sort based on the frequencies and return top K but this approach would take time of O(NlogN). If we use heap here, we can reduce time to O(Nlogk).
        if k == len(nums):  # Optimization to avoid O(NlogN) when k equals length of nums.
            return nums
        freq_map = Counter(nums)  # Time and Space: O(N)
        min_heap = []
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))  # Time: O(Nlogk), Space: O(k)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for freq, num in min_heap]  # Time: O(klogk)
        """
        # Approach 2: Bucket sort which leads to Time: O(N) which is better than O(Nlogk) provided by Approach 1.
        if k == len(nums):  # Optimization to avoid O(NlogN) when k equals length of nums.
            return nums
        freq_map = Counter(nums)

        # Initialize buckets: List of lists where index represents freq. Length is len(nums) + 1 because max frequency can be len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            buckets[freq].append(num)

        # Flatten the buckets into a single list. Iterate backwards from the highest frequency bucket to the lowest
        flattened = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                flattened.append(num)

        return flattened[:k]
