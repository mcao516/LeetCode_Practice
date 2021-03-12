# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None and root2 is None:
            return None
        if root1 and root2 is None:
            return root1
        if root1 is None and root2:
            return root2
        
        queue_1, queue_2 = [root1], [root2]
        
        while len(queue_1) > 0:
            node_1 = queue_1.pop(0)
            node_2 = queue_2.pop(0)
            
            node_1.val = node_1.val + node_2.val
            
            if node_1.left and node_2.left:
                queue_1.append(node_1.left)
                queue_2.append(node_2.left)

            if node_1.right and node_2.right:
                queue_1.append(node_1.right)
                queue_2.append(node_2.right)
                
            if node_1.left is None and node_2.left:
                node_1.left = node_2.left
                
            if node_1.right is None and node_2.right:
                node_1.right = node_2.right
        
        return root1