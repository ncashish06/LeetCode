from collections import Counter, deque
import heapq


class Solution:
    # Date Solved: 9 May 2026, Saturday
    """
    Similarity to LC767 (Reorganize String):
        - LC358 is the generalized version of LC767; setting k=2 in LC358 solves LC767
        - The heap + cooldown pattern is identical — the only difference is cooldown size:
            LC767: prev (single slot, cooldown = 1)
            LC358: deque of size k (cooldown = k-1 slots before a char is re-eligible)
        - LC767's Approach 2 (odd/even) and Approach 3 (greedy top two) do not generalize here
          because a fixed index layout only works when k=2
    """

    def rearrangeString(self, s: str, k: int) -> str:
        # Time: O(n log k) and Auxiliary Space: O(k) — heap + cooldown queue at most k unique characters
        if k == 0:
            return s  # No constraint, any arrangement works

        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        queue = deque()  # Cooldown window — holds (cnt, char) for k steps before re-eligibility

        res = ""
        while len(res) < len(s):  # Stop when result is complete
            if not maxHeap:
                return ""  # Characters stuck in cooldown with no valid next char

            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1  # Increment since counts are negative

            queue.append((cnt, char))  # Enter cooldown

            if len(queue) == k:  # Oldest char has served its k-step cooldown
                cnt, char = queue.popleft()
                if cnt != 0:
                    heapq.heappush(maxHeap, [cnt, char])  # Re-eligible for placement

        return res
