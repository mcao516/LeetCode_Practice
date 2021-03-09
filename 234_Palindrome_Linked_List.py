# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        middle = self.find_the_middle(head)
        self.reverse_linklist(middle)
        
        sec_pointer = middle.next
        while head is not None and sec_pointer is not None:
            if sec_pointer.val != head.val:
                return False
            sec_pointer = sec_pointer.next
            head = head.next
        
        return True
        
    def reverse_linklist(self, head):
        current = head.next
        head.next = None
        
        while current is not None:
            next_to_add = current.next
            current.next = head.next
            head.next = current
            current = next_to_add        
    
    def find_the_middle(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow