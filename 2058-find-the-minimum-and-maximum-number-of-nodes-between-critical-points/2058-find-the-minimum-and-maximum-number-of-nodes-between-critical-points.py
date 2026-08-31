# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Date Solved: 31 August 2026, Monday, POTD
    # Refer: codestorywithMIK and NeetCode
    # In NC All
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def critical(prev, cur, nxt):
            return prev.val > cur.val < nxt.val or prev.val < cur.val > nxt.val

        prev, cur = head, head.next
        nxt = cur.next
        min_dist, max_dist = float("inf"), -1
        prev_crit_idx = 0
        first_crit_idx = 0
        i = 1  # index of cur
        while nxt:
            if critical(prev, cur, nxt):
                if first_crit_idx:
                    max_dist = i - first_crit_idx
                    min_dist = min(min_dist, i - prev_crit_idx)
                else:
                    first_crit_idx = i
                prev_crit_idx = i

            prev, cur, nxt = cur, nxt, nxt.next
            i += 1

        if min_dist == float("inf"):
            min_dist = -1
        return [min_dist, max_dist]
