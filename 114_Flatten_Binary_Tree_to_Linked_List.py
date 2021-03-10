# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None: return None
        
        visited = []
        self.pre_order(root, visited)
        
        for i in range(len(visited) - 1):
            visited[i].left = None
            visited[i].right = visited[i+1]
            
        visited[-1].left = None
        visited[-1].right = None
        
    def pre_order(self, root, visited):
        if root is not None:
            visited.append(root)
            self.pre_order(root.left, visited)
            self.pre_order(root.right, visited)
        