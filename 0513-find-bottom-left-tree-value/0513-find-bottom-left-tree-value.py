# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
      def reflected_bfs(root):
        ans = root.val
        queue = deque()
        queue.append(root)
        while len(queue):
          node = queue.popleft()
          if node.right: queue.append(node.right)
          if node.left: queue.append(node.left)
          ans = node.val
        
        return ans
      
      return reflected_bfs(root)