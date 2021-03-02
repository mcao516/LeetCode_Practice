# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        visited = []
        self.inOrderTraversal(root, visited)
        return visited[k-1]
    
    def inOrderTraversal(self, root: TreeNode, visited: List):
        if root is not None:
            self.inOrderTraversal(root.left, visited)
            visited.append(root.val)
            self.inOrderTraversal(root.right, visited)