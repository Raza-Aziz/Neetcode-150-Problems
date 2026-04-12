# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head

        # Step 1 :: Find middle point of list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast.next is None:
                break

        # Step 2 :: Reverse from slow
        curr = slow.next
        prev = None
        slow.next = None

        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next

        # Step 3 :: Combine both
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first, second = temp1, temp2
