# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    a = self.deConstruct(root)

    b = a + [val]

    return self.Construct(b)

  def deConstruct(self, node):
    if node is None: return []
    return self.deConstruct(node.left) + [node.val] + self.deConstruct(node.right)
  
  def Construct(self, b):
    if len(b) == 0: return None
    m, p = 0, 0
    for i, v in enumerate(b):
      if v > m:
        m = v
        p = i
    
    root = TreeNode(m, self.Construct(b[:p]), self.Construct(b[p + 1:]))

    return root


        