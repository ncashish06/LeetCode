class Solution:
    # Date Solved: 12 July 2026, Sunday, POTD
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        val_idx_map = {}
        n = len(arr)
        result = [0] * n
        for idx, val in enumerate(arr):
            if val in val_idx_map:
                val_idx_map[val].append(idx)
            else:
                val_idx_map[val] = [idx]
        arr.sort()
        current_rank = 0
        for _, val in enumerate(arr):
            if val in val_idx_map:
                current_rank += 1
                output_indices = val_idx_map.pop(val)
                for i in range(len(output_indices)):
                    result[output_indices[i]] = current_rank
        return result
