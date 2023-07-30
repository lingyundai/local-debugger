from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                # [isbalanced, Hdiff]
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            height = abs(left[1] - right[1])

            balanced = (left[0] and right[0] and height <= 1)

            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]

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

root = [3,9,20,None,None,15,7]
s = Solution()
print(s.isBalanced(fromlist(root)))