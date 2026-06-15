# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Date Solved: 15 June 2026, Monday
    # Blind 75
    # Refer: codestorywithMIK
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        # Approach 1: Two pass with Time: O(n)
        def lengthLinkedList(node):
            l = 0
            while node:
                l += 1
                node = node.next
            return l

        length = lengthLinkedList(head)
        # nth from end = first node, so just return head.next
        if length == n:
            return head.next

        temp = head
        prev = None
        travel = length - n
        while travel:
            prev = temp
            temp = temp.next
            travel -= 1
        # Skip over the target node
        prev.next = temp.next
        return head
        """
        # Approach 2: One pass with Time: O(n)
        fast = head
        slow = head

        # Move fast n steps ahead so the gap between slow and fast is exactly n
        for i in range(n):
            fast = fast.next

        # If fast is None, the nth from end is the head itself
        if not fast:
            return head.next

        # Move both until fast reaches the last node
        # slow will be just before the node to delete
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        # Skip over the target node
        slow.next = slow.next.next

        return head
        