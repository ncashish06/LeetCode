# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Date Solved: 14 June 2026, Sunday, POTD
    # Refer: codestorywithMIK for Approach 1 and 2, NeetCode for Approach 3
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        # Approach 1: Using a List
        # Time: O(n), Space: O(n)
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        i, j = 0, len(vals) - 1
        result = 0
        while i < j:
            result = max(result, vals[i] + vals[j])
            i += 1
            j -= 1
        return result

        # Approach 2: Using a stack
        # Time: O(n), Space: O(n)
        st = []
        curr = head
        while curr:
            st.append(curr.val)
            curr = curr.next

        curr = head
        N = len(st)
        result = 0
        for _ in range(N // 2):
            result = max(result, curr.val + st.pop())
            curr = curr.next
        return result
        """
        # Approach 3: Reverse First Half In-Place
        # Time: O(n), Space: O(1)
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return res
