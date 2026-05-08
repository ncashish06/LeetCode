class Solution:
    from collections import defaultdict, deque
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
            
        # ── Step 1: Sieve of Eratosthenes ────────────────────────────────────────
        # Precompute primes up to max(nums) so we can check primality in O(1)
        max_val = max(nums)
        is_prime = [False, False] + [True] * (max_val - 1)  # index = number
        for i in range(2, int(max_val**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, max_val + 1, i):
                    is_prime[j] = False

        # ── Step 2: Build prime buckets ──────────────────────────────────────────
        # bucket[p] = list of all indices j where nums[j] is divisible by prime p
        # Used for teleportation: if standing on prime p, jump to any index in bucket[p]
        bucket = defaultdict(list)
        for j in range(n):
            # Each nums[j] can have multiple prime factors
            # e.g. nums[j]=12 → factors 2,3 → add j to bucket[2] and bucket[3]
            val = nums[j]
            d = 2
            temp = val
            while d * d <= temp:
                if temp % d == 0:
                    if is_prime[d]:
                        bucket[d].append(j)
                    while temp % d == 0:
                        temp //= d
                d += 1
            if temp > 1 and is_prime[temp]:   # remaining prime factor
                bucket[temp].append(j)

        # ── Step 3: BFS from index 0 to index n-1 ───────────────────────────────
        visited = [False] * n
        visited[0] = True
        queue = deque([0])
        jumps = 0

        while queue:
            jumps += 1

            # Process all nodes at current BFS level (same jump count)
            for _ in range(len(queue)):
                i = queue.popleft()

                # --- Move type 1: Adjacent steps ---
                for neighbor in [i - 1, i + 1]:
                    if 0 <= neighbor < n and not visited[neighbor]:
                        if neighbor == n - 1:
                            return jumps
                        visited[neighbor] = True
                        queue.append(neighbor)

                # --- Move type 2: Prime teleportation ---
                # If nums[i] is prime p, teleport to all unvisited indices in bucket[p]
                # Since nums[i] itself could be prime, use it directly
                p = nums[i]
                if is_prime[p] and bucket[p]:
                    # Visit all indices divisible by p in one BFS level
                    for j in bucket[p]:
                        if not visited[j]:
                            if j == n - 1:
                                return jumps
                            visited[j] = True
                            queue.append(j)
                    # Clear bucket — these nodes are now reachable, no need to
                    # revisit via teleportation again (key optimization!)
                    bucket[p].clear()

        return jumps