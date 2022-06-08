# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(-1, head)
        left = dummy_head
        right = head 

        while n > 0 and right: 
            right = right.next
            n-=1

        while right:
                right = right.next
                left = left.next

        # delete
        left.next = left.next.next
        return dummy_head.next
        