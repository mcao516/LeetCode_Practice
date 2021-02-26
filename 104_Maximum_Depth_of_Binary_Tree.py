# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        
        root.height = 0
        queue = [root]
        
        max_depth = 0
        while(len(queue) > 0):
            node = queue.pop(0)
            
            if node.height + 1 > max_depth:
                max_depth = node.height + 1
            
            if node.left is not None:
                node.left.height = node.height + 1
                queue.append(node.left)
                
            if node.right is not None:
                node.right.height = node.height + 1
                queue.append(node.right)
        
        return max_depth