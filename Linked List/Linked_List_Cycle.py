# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Two pointer ::
        # fast goes 2 steps, slow goes 1 step (at a time)
        # If fast == slow, then a cycle
        fast = head
        slow = head

        if not head or head.next is None:
            return False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

        # Using set :: if exists in set, then visited
        freq = set()

        if not head or head.next is None:
            return False

        while head:
            if head in freq:
                return True
            else:
                freq.add(head)
                head = head.next
        return False
