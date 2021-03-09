# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pointer_1, pointer_2 = head, head
        
        i = 0
        while pointer_1 is not None and pointer_2 is not None:
            pointer_1 = pointer_1.next
            
            if i % 2 == 1:
                pointer_2 = pointer_2.next
                
            i += 1
                
            if pointer_1 == pointer_2:
                return True
        
        return False