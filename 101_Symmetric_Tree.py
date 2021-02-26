# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         return root is None or self.isSame(root.left, root.right)
    
#     def isSame(self, left: TreeNode, right: TreeNode) -> bool:
#         if left is None and right is None:
#             return True
#         elif left is None or right is None:
#             return False
#         elif left.val != right.val:
#             return False
#         else:
#             return self.isSame(left.left, right.right) and self.isSame(left.right, right.left)
 
        
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        traversal = []
        root.level = 0
        
        queue = []
        queue.append(root)
        max_depth = 0
        while(len(queue) > 0):
            node = queue.pop(0)
            
            if type(node) == type(1):
                if node + 1 > len(traversal):
                    traversal.append([])
                traversal[node].append(None)
                continue
            else:
                if node.level + 1 > len(traversal):
                    traversal.append([])
                traversal[node.level].append(node.val)
                
                if node.level + 1 > max_depth:
                    max_depth = node.level + 1
            
            if node.left is not None:
                node.left.level = node.level + 1
                queue.append(node.left)
            else:
                queue.append(node.level + 1)
                
            if node.right is not None:
                node.right.level = node.level + 1
                queue.append(node.right)
            else:
                queue.append(node.level + 1)

        
        traversal = traversal[:max_depth]
        for t in traversal:
            if not self.checkListSymmetric(t):
                return False
        return True
        
        
    def checkListSymmetric(self, l):
        if len(l) == 1:
            return True
        else:
            assert len(l) % 2 == 0
            for i in range(0, len(l) // 2):
                if l[i] != l[len(l) - 1 - i]:
                    return False
            return True
            
        
        