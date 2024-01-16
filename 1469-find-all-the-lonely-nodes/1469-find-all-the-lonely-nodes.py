# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
      return self.dfs(root)
        
    def dfs(self, node):
      if node == None: return []
      dfs_left = self.dfs(node.left)
      dfs_right = self.dfs(node.right)
      if node.left == None and node.right: dfs_right.append(node.right.val)
      if node.right == None and node.left: dfs_left.append(node.left.val)
      return dfs_left + dfs_right