class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        for _ in range(volume):
            for d in (-1, 1):
                i = best = k
                while 0 <= i + d < len(heights) and heights[i + d] <= heights[i]:
                    if heights[i + d] < heights[i]:
                        best = i + d
                    i += d
                if best != k:
                    heights[best] += 1
                    break
            else:
                heights[k] += 1
        return heights
