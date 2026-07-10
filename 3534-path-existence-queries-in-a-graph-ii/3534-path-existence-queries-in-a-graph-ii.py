class Solution:
    # Date Solved: 10 July 2026, Friday, POTD
    # Refer: codestorywithMIK
    # Brute force approaches such as BFS, Dijkstra's, Floyd Warshall are all expensive, so going for Binary Lifting
    # Time: O(N*logN + Q*logN), Space: O(N*logN)
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        def customUpperBound(arr: List[tuple], target: int) -> int:
            l, r = 0, len(arr) - 1
            result = 0
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid][0] <= target:
                    result = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return result

        arr = sorted((nums[i], i) for i in range(n))
        nodeToIdx = [0] * n
        for i in range(n):
            node = arr[i][1]
            nodeToIdx[node] = i

        rows = n
        cols = int(math.log2(n)) + 1
        ancestorTable = [[0] * cols for _ in range(rows)]

        # Fill 0th column first
        for node in range(n):  # nlogn
            farthestIdxOneHop = customUpperBound(arr, arr[node][0] + maxDiff)
            ancestorTable[node][0] = farthestIdxOneHop

        # Fill remaining columns
        for j in range(1, cols):  # logn
            for node in range(n):  # n
                ancestorTable[node][j] = ancestorTable[ancestorTable[node][j - 1]][j - 1]

        result = []
        for u, v in queries:  # O(q)
            a = nodeToIdx[u]
            b = nodeToIdx[v]
            if a == b:
                result.append(0)
                continue

            if a > b:
                a, b = b, a

            curr = a
            jumps = 0

            for j in range(cols - 1, -1, -1):  # log(n)
                if ancestorTable[curr][j] < b:
                    curr = ancestorTable[curr][j]
                    jumps += 1 << j  # pow(2, j)

            if ancestorTable[curr][0] >= b:
                result.append(jumps + 1)
            else:
                result.append(-1)

        return result
