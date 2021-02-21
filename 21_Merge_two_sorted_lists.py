# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        if l1 is None: return l2
        if l2 is None: return l1
        
        pointer_1, pointer_2 = l1, l2
        if l1.val <= l2.val:
            sorted_list = l1
            pointer_1 = pointer_1.next
        else:
            sorted_list = l2
            pointer_2 = pointer_2.next
        sorted_list.next = None
        origin_pointer = sorted_list
        
        while pointer_1 and pointer_2:
            if pointer_1.val <= pointer_2.val:
                sorted_list.next = pointer_1
                sorted_list = sorted_list.next
                pointer_1 = pointer_1.next
            else:
                sorted_list.next = pointer_2
                sorted_list = sorted_list.next
                pointer_2 = pointer_2.next
                
        if pointer_2 is None:
            sorted_list.next = pointer_1
        elif pointer_1 is None:
            sorted_list.next = pointer_2
            
        return origin_pointer
    