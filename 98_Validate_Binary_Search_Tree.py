# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        visited = []
        self.inOrderTraversal(root, visited)
        print(visited)
        
        for i in range(1, len(visited)):
            if visited[i] <= visited[i-1]:
                return False
        return True
    
    def inOrderTraversal(self, root: TreeNode, visited: List):
        if root is not None:
            self.inOrderTraversal(root.left, visited)
            visited.append(root.val)
            self.inOrderTraversal(root.right, visited)