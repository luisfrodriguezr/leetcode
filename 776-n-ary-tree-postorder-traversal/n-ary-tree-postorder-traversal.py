"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
  def postorder(self, root: 'Node') -> List[int]:
    return self.dfs(root)

  def dfs(self, node):
    if node is None: return []
    ans = list()

    for child in node.children:
      ans += self.dfs(child)

    return ans + [node.val]
        