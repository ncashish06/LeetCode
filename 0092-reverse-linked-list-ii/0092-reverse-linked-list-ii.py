# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Date Solved: 15 June 2026, Monday
    # NC250
    # Refer: codestorywithMIK, problems like these in linked list are tricky, try to draw and visualize
    # Time: O(n), Space: O(1)
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Dummy node points to head, so prev can start before the list
        dummy = ListNode(0)
        dummy.next = head

        # Move prev to the node just before position 'left'
        prev = dummy
        for i in range(1, left):
            prev = prev.next

        # curr is the node at position 'left' (first node to be reversed)
        curr = prev.next

        # Perform right-left insertions to reverse the sublist
        for i in range(right - left):
            temp = prev.next  # 0: save current front of reversed portion
            prev.next = curr.next  # 1: detach curr's next, make prev point to it
            curr.next = curr.next.next  # 2: curr skips over the node we just moved
            prev.next.next = temp  # 3: inserted node points to old front of reversed portion
            
        return dummy.next
