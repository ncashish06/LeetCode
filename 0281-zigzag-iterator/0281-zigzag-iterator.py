from collections import deque


class ZigzagIterator:
    # Date Solved: 25 April 2026, Saturday
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = deque()
        for v in [v1, v2]:
            if v:
                self.queue.append([v, 0])

    def next(self) -> int:
        v, i = self.queue.popleft()
        res = v[i]

        if i + 1 < len(v):
            self.queue.append([v, i + 1])

        return res

    def hasNext(self) -> bool:
        return len(self.queue) > 0


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
