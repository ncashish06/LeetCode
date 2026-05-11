class Solution:
    # Date Solved: 10 May 2026, Sunday
    # Refer: Namaste DSA and NeetCode 150 solution.
    # This is a variation of LC767 Reorganize String but we don't need heap here.
    # The most frequent tasks drives everything.
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        # Approach 1: Math based by Namaste DSA but this is less intuitive to come up during an interview
        # Time: O(N) where N = Number of tasks
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord("A")] += 1

        maxf = max(count)
        maxFreqElements = 0
        for i in count:
            maxFreqElements += 1 if i == maxf else 0

        time = (maxf - 1) * (n + 1) + maxFreqElements
        return max(len(tasks), time)
        """
        # Approach 2: Max-Heap and Cooldown Queue by NeetCode
        # Time: O(N) where N = Number of tasks, Heap operations are O(log(26)) so constant time.
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of (remaining_count_after_running, next_available_time)
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # Since Python has only min heap, we store -ve. We increase each time till
                if cnt:
                    q.append([cnt, time + n]) # (remaining_count_after_running, next_available_time)
            if q and q[0][1] == time: # next_available_time == time
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
        