# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Date Solved: 15 June 2026, Monday, POTD
    # Refer: Solved on my own
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: # if only one node then delete it
            return None
        prev, slow, fast = None, head, head
        while fast and fast.next:  # fast.next.next can be the last node or None (node after the last node)
            fast = fast.next.next
            prev = slow
            slow = slow.next

        prev.next = slow.next
        return head
