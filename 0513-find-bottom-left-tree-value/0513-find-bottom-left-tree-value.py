# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
      def dfs(node):
        if node is None:
          return 0
        left = dfs(node.left)
        right = dfs(node.right)
        if right > left: 
          if node.right is not None:
            node.val = node.right.val
          return right + 1
        else:
          if node.left is not None:
            node.val = node.left.val
          return left + 1
      dfs(root)
      return root.val