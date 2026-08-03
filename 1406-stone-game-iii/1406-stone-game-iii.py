class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        # t[i] = best (Alice - Bob) score difference achievable 
        # starting from index i onward
        t = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            t[i] = stoneValue[i] - t[i + 1]
            
            if i + 2 <= n:
                t[i] = max(t[i], stoneValue[i] + stoneValue[i + 1] - t[i + 2])
            
            if i + 3 <= n:
                t[i] = max(t[i], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - t[i + 3])
        
        diff = t[0]
        
        if diff < 0:
            return "Bob"
        elif diff > 0:
            return "Alice"
        
        return "Tie"