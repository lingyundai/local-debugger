from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, left, right):
            if not root:
                return True
            
            if not (left < root.val < right):
                return False
            
            return (dfs(root.left, left, root.val)
                and dfs(root.right, root.val, right))
        
        return dfs(root, float("-inf"), float("inf"))

def fromlist(values):
    def create(it):
        value = next(it)
        return None if value is None else TreeNode(value)
        
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    nextlevel = [root]
    try:
        while nextlevel:
            level = nextlevel
            nextlevel = []
            for node in level:
                if node:
                    node.left = create(it)
                    node.right = create(it)
                    nextlevel += [node.left, node.right]
        
    except StopIteration:
        return root
    raise ValueError("Invalid list")

root = [2,1,3]
s = Solution()
print(s.isValidBST(root));