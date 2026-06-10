# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # Date Solved: 10 June 2026, Wednesday
    # Blind 75
    # Refer: codestorywithMIK
    # I also referred to NeetCode (no Namaste DSA solution) — which provides the same iterative version.
    # Time: O(N log k) — k is the total number of lists, N is the total number of nodes across all k lists
    # Space: O(N) worst case — O(log k) from partitionAndMerge's call stack, but mergeTwoSortedLists
    #        can go O(N) deep if one merged list is very long. O(log k) if list lengths are balanced.
    # mergeTwoSortedLists is the solution to LC 21. Merge Two Sorted Lists (Easy - Blind 75)
    def mergeTwoSortedLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        # Use this for interview: I implemented the iterative version since max recursion depth exceeded
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoSortedLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoSortedLists(l1, l2.next)
            return l2
        """
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

    def partitionAndMerge(
        self, start: int, end: int, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        if start == end:
            return lists[start]
        if start > end:
            return None

        mid = start + (end - start) // 2

        l1 = self.partitionAndMerge(start, mid, lists)
        l2 = self.partitionAndMerge(mid + 1, end, lists)

        return self.mergeTwoSortedLists(l1, l2)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        return self.partitionAndMerge(0, n - 1, lists)
