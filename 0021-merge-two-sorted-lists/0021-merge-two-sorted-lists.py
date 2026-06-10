# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # Date Solved: 10 June 2026, Wednesday
    # Blind 75
    # Refer: codestorywithMIK
    # I also referred to NeetCode and Namaste DSA — both provide the same iterative version.
    # Time: O(m+n) — total number of nodes across both lists
    # Space: O(m+n) — recursive call stack depth in the worst case (ignoring this, O(1))
    # Also used as a helper in LC 23. Merge k Sorted Lists (Hard - Blind 75)
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        """
        # Iterative version
        dummy = ListNode(-1)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next
        """
