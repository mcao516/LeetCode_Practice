# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        traversal = []
        
        root.level = 0
        
        queue = []
        queue.append(root)
        
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
                
        return traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []
        if root is None:
            return output
        
        queue = [root]
        while(len(queue) > 0):
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            
            output.append(level)
        
        return output

