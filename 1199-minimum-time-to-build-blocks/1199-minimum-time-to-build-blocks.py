class Solution:
    # Date Solved: 1 August 2026, Saturday, Weekly Premium W1
    # Refer: Claude
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heapq.heapify(blocks)

        while len(blocks) > 1:
            a = heapq.heappop(blocks)
            b = heapq.heappop(blocks)
            # a <= b since it's a min-heap; a's split cost gets hidden under b
            heapq.heappush(blocks, b + split)

        return blocks[0]
