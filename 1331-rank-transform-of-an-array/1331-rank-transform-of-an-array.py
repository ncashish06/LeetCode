class Solution:
    # Date Solved: 12 July 2026, Sunday, POTD
    # Time: O(nlogn), Space: O(n)
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Both mine and codestorywithMIK's solution have same Time and Space
        """
        # My solution
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
        """
        # codestorywithMIK solution
        temp = sorted(arr)
        n = len(arr)
        result = []
        
        rank_map = {}
        rank = 1
        for i, val in enumerate(temp):
            if i > 0 and val > temp[i - 1]:
                rank += 1
            rank_map[val] = rank

        for val in arr:
            result.append(rank_map[val])
        return result
