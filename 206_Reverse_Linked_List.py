# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        # get the end node
        end = head
        while end.next is not None:
            end = end.next
        
        temp = head
        while temp != end:
            to_add = temp
            temp = temp.next
            
            to_add.next = end.next
            end.next = to_add
            
        return end