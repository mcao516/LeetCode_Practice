# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        visited = []
        self.DFS(root, visited)
        return visited
    
    def DFS(self, root, visited):
        if root is not None:
            self.DFS(root.left, visited)
            visited.append(root.val)
            self.DFS(root.right, visited)


class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        visited, stack = [], []
        
        while (root is not None) or (len(stack) > 0):
            while root is not None:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            visited.append(root.val)
            root = root.right
            
        return visited
