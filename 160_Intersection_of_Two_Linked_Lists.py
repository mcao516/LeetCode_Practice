# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = self.calculate_len(headA)
        lenB = self.calculate_len(headB)
        
        while lenA != lenB:
            if lenA > lenB:
                headA = headA.next
                lenA -= 1
            else:
                headB = headB.next
                lenB -= 1
                
        while headA != headB:
            headA = headA.next
            headB = headB.next
            
        return headA
        
    def calculate_len(self, head):
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length