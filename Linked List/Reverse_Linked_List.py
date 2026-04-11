# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # --- NOTE: Iterative Approach
        curr, prev = head, None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

        # --- NOTE: Recursive Approach
        if not head:
            return None

        new_head = head

        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return new_head


# 1. RECURSIVE DIVE: Go to the end of the list first.
#    - If head is 1, call reverse(2). If 2, call reverse(3).
#    - This builds a stack of "paused" functions.

# 2. BASE CASE: Reach the tail (Node 3).
#    - Node 3 has no 'next', so it becomes 'new_head' and returns.

# 3. THE UNWIND (Back at Node 2):
#    - 'head' is 2, 'head.next' is 3.
#    - head.next.next = head: Make 3 point back to 2.
#    - head.next = None: Break 2's original link to 3.

# 4. THE UNWIND (Back at Node 1):
#    - 'head' is 1, 'head.next' is 2.
#    - head.next.next = head: Make 2 point back to 1.
#    - head.next = None: Break 1's original link to 2.

# 5. FINAL RETURN:
#    - Pass 'new_head' (Node 3) all the way up to the original caller.
