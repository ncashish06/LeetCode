from collections import deque

class Solution:
    # Date Solved: 25 May 2026, Monday, POTD
    # NC250, Refer: NeetCode
    # Time: O(n), Space: O(n)
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # Approach: BFS since this is reachability problem
        # Early exit: last index is '1', can never land on it
        if s[-1] == '1':
            return False

        # BFS from index 0 (guaranteed to be '0' per constraints)
        q = deque([0])

        # Tracks the farthest index whose jump window has been fully scanned.
        # Used as the left boundary of the next scan to avoid re-processing
        # indices that were already considered — replaces a visited array.
        farthest = 0

        while q:
            i = q.popleft()

            # Sliding window trick: start scanning from whichever is further —
            #   i + minJump : minimum jump distance from current index
            #   farthest + 1: skip indices already scanned by previous nodes
            # This ensures each index is enqueued at most once -> O(n) total
            start = max(i + minJump, farthest + 1)

            for j in range(start, min(i + maxJump + 1, len(s))):
                if s[j] == '0':
                    q.append(j)

                    # BFS guarantees first time we reach last index = valid path
                    if j == len(s) - 1:
                        return True

            # Mark everything up to i+maxJump as scanned.
            # Any future node won't need to re-scan this range.
            farthest = i + maxJump

        # Exhausted all reachable indices without hitting last index
        return False