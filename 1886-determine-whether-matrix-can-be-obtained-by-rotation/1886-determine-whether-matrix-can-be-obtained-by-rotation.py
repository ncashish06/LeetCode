class Solution:
    # Check Leetcode 48. Rotate Image
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
        for k in range(4):
            if mat == target:
                return True
            # Same rotation logic as LC 48
            for i in range(n // 2 + n % 2):
                for j in range(n // 2):
                    tmp = mat[n - 1 - j][i]
                    mat[n - 1 - j][i] = mat[n - 1 - i][n - j - 1]
                    mat[n - 1 - i][n - j - 1] = mat[j][n - 1 - i]
                    mat[j][n - 1 - i] = mat[i][j]
                    mat[i][j] = tmp
        
        return False