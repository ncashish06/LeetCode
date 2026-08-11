class Solution:
    # Date Solved: 10 August 2026, Monday, Weekly Premium W2
    # Refer: Claude
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        # Approach - Lowest Common Ancestor (LCA) in a forest
        # Time: O(n) to build parent map + O(h) to walk up (h = height of tree)
        # Space: O(n) for the parent map and ancestor set
        parent = {}  # child -> parent mapping
        for region in regions:
            for i in range(1, len(region)):
                parent[region[i]] = region[0]

        # Collect all ancestors of region1 (including itself)
        ancestors1 = set()
        node = region1
        while node in parent:
            ancestors1.add(node)
            node = parent[node]
        ancestors1.add(node)  # add the root too

        # Walk up from region2 until we hit a common ancestor
        node = region2
        while node not in ancestors1:
            node = parent[node]

        return node
