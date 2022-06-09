# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        left, right = head, head.next
        # after while loop, left.next will be the head of 2nd half of linked list
        while right and right.next:
            left = left.next
            right = right.next.next

        # rever 2nd half linked list   
        curr = left.next 
        prev = left.next = None
        while curr: 
            post = curr.next
            curr.next = prev 
            prev = curr
            curr = post 
        head_2 = prev

        # Merge two list
        first, second = head, head_2
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
       


        