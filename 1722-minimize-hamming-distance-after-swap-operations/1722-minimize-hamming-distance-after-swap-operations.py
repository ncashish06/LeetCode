from collections import defaultdict


class Solution:
    # Date Solved: 20 April 2026, Monday
    # Refer Namaste DSA, Kruskal + Union Find Code
    # Time Complexity: O((N + S).α(N)), where N is the length of the array and S is the number of allowed swaps. α is the Inverse Ackermann function, making the Union-Find operations effectively constant time.
    # The amortized time complexity for union-find by rank and path compression is O(α(N)), where α(N) is Inverse Ackermann Function, which is nearly constant, even for large values of N.
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)

        # Initialize the Union-Find 'parent' array.
        # Initially, every index is its own parent (each node is its own group).
        parent = list(range(n))

        # 1. Union-Find: 'find' function with Path Compression.
        # Path compression flattens the tree structure, making future lookups nearly O(1).
        def find(i):
            if parent[i] == i:
                return i
            # Recursively find the root and update parent[i] to point directly to the root.
            parent[i] = find(parent[i])
            return parent[i]

        # 1. Union-Find: 'union' function to connect two indices.
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                # Merge the two sets by pointing one root to the other.
                parent[root_i] = root_j

        # 2. Process all allowed swaps.
        # Every swap represents an edge in a graph. Indices connected by swaps
        # form a 'connected component' where elements can be moved to any index in that group.
        for a, b in allowedSwaps:
            union(a, b)

        # 3. Group the available values by their connected components.
        # Key: The 'root' index of the component.
        # Value: A frequency map (bag) of all numbers available in 'source' for that group.
        components = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            root = find(i)
            # Add the source element at this index to its component's pool.
            components[root][source[i]] += 1

        # 4. Calculate the Minimum Hamming Distance.
        # We check each position in the target to see if the required number
        # exists in the available pool for that position's component.
        distance = 0
        for i in range(n):
            root = find(i)
            val = target[i]

            # If the target value exists in the 'bag' for this component, use it.
            if components[root][val] > 0:
                components[root][val] -= 1
            else:
                # If the value isn't available in this component's bag,
                # it means we cannot move a matching number to this index.
                distance += 1

        return distance
