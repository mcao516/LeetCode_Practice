# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        elif l1 is None and l2 is not None:
            return l2
        elif l1 is not None and l2 is None:
            return l1
        
        start = curr = ListNode(val=-1)
        
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
            else:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
                
        while l1:
            curr.next = l1
            curr = curr.next
            l1 = l1.next
            
        while l2:
            curr.next = l2
            curr = curr.next
            l2 = l2.next
            
        return start.next
    

