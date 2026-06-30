class TreeAncestor:
    # Date Solved: 12 June 2026, Friday
    # Refer: codestorywithMIK Binary Lifting (DP) playlist, 2nd of 4 videos
    # Related to today's POTD
    # Time : O(Q * log(n)) , Q = number of queries , n = number of nodes
    # Space : O(n * log(n)) to store events in map
    def __init__(self, n: int, parent: List[int]):
        self.cols = int(math.log2(n)) + 1
        self.ancestor_table = [[-1] * self.cols for _ in range(n)]

        # Fill the 0th column first - immediate parent (ancestor)
        for node in range(n):
            self.ancestor_table[node][0] = parent[node]

        for j in range(1, self.cols):
            for node in range(n):
                if self.ancestor_table[node][j - 1] != -1:
                    self.ancestor_table[node][j] = self.ancestor_table[self.ancestor_table[node][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.cols):
            if k & (1 << j):  # jth bit is set so we can take 2^j jump
                node = self.ancestor_table[node][j]
                if node == -1:
                    return -1

        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
