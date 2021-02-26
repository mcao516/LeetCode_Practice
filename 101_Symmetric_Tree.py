# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return root is None or self.isSame(root.left, root.right)
    
    def isSame(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        elif left.val != right.val:
            return False
        else:
            return self.isSame(left.left, right.right) and self.isSame(left.right, right.left)