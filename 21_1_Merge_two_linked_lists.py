# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        
        pointer_1, pointer_2 = l1, l2
        
        if l1 is not None:
            sorted_list = l1
            pointer_1 = pointer_1.next
            sorted_list.next = None
        else:
            sorted_list = l2
            pointer_2 = pointer_2.next
            sorted_list.next = None
            
        while pointer_1 is not None:
            node_to_add = pointer_1
            pointer_1 = pointer_1.next
            
            sorted_list = self.add_value(node_to_add, sorted_list)
            
        while pointer_2 is not None:
            node_to_add = pointer_2
            pointer_2 = pointer_2.next
            
            sorted_list = self.add_value(node_to_add, sorted_list)
            
        return sorted_list
            
    def add_value(self, node_to_add, sorted_list):
        pointer = sorted_list
        if node_to_add.val <= pointer.val:
            node_to_add.next = pointer
            return node_to_add
        else:
            while pointer is not None and node_to_add.val > pointer.val:
                pre_pointer = pointer
                pointer = pointer.next
                
            pre_pointer.next = node_to_add
            node_to_add.next = pointer
            return sorted_list


if __name__ == '__main__':
    def print_list(l):
        while l is not None:
            print('{} - '.format(l.val), end='')
            l = l.next
        print()
        
    node_a = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4)))
    node_b = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))

    print_list(node_a)
    print_list(node_b)
    print_list(Solution().mergeTwoLists(node_a, node_b))