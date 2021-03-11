# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_map = {v: i for i, v in enumerate(inorder)}
        return self.helper(preorder, 0, len(preorder)-1, 0, len(inorder)-1, inorder_map)
        
    def helper(self, preorder, preLeft, preRight, inLeft, inRight, inorder_map):
        if preLeft > preRight or inLeft > inRight:
            return None
        
        root_value = preorder[preLeft]
        root = TreeNode(root_value)
        pIndex = inorder_map[root_value]
        
        root.left = self.helper(preorder, preLeft + 1, preLeft + pIndex - inLeft, inLeft, pIndex-1, inorder_map)
        root.right = self.helper(preorder, preLeft + 1 + pIndex - inLeft, preRight, pIndex+1, inRight, inorder_map)
        
        return root