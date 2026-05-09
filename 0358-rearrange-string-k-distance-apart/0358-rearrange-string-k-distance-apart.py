from collections import Counter, deque
import heapq


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        # Time: O(n log k) | Auxiliary Space: O(k) — heap + cooldown queue
        if k == 0:
            return s  # No constraint, any arrangement works

        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        queue = deque()  # Cooldown window — holds (cnt, char) for k steps

        res = ""
        while len(res) < len(s):  # Stop when result is complete
            if not maxHeap:
                return ""  # Characters stuck in cooldown, impossible

            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1  # Increment since counts are negative

            queue.append((cnt, char))  # Enter cooldown

            if len(queue) == k:  # Oldest char has served its cooldown
                cnt, char = queue.popleft()
                if cnt != 0:
                    heapq.heappush(maxHeap, [cnt, char])  # Re-eligible for placement

        return res
