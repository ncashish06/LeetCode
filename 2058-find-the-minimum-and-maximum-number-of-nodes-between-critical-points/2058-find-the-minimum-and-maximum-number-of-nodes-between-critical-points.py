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
        min_distance = float("inf")

        prev = head
        curr = head.next
        curr_position = 1
        previous_critical_index = 0
        first_critical_index = 0

        while curr.next is not None:
            # When we see a critical point
            if (curr.val < prev.val and curr.val < curr.next.val) or (
                curr.val > prev.val and curr.val > curr.next.val
            ):

                if previous_critical_index == 0:
                    previous_critical_index = curr_position
                    first_critical_index = curr_position
                else:
                    min_distance = min(
                        min_distance, curr_position - previous_critical_index
                    )
                    previous_critical_index = curr_position

            curr_position += 1
            prev = curr
            curr = curr.next

        if min_distance == float("inf"):
            return [-1, -1]

        max_distance = previous_critical_index - first_critical_index
        return [min_distance, max_distance]
