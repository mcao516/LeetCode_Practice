# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [root.val]
        
        queue = []
        queue.append(root)
        traversal = []
        
        root.level = 0
        while(len(queue) > 0):
            node = queue.pop(0)
            
            if node.level + 1 > len(traversal):
                traversal.append([])
            traversal[node.level].append(node.val)
            
            if node.left is not None:
                node.left.level = node.level + 1
                queue.append(node.left)
            
            if node.right is not None:
                node.right.level = node.level + 1
                queue.append(node.right)
            
        return [l[-1] for l in traversal]