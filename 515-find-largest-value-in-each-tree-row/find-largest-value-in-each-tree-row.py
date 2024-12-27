# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans = list()
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = list()
        self.dfs(root, 0)

        return self.ans

    def dfs(self, node, rank):
        if node is not None:
            while len(self.ans) <= rank:
                self.ans.append(-(2 ** 31) - 1)
            self.ans[rank] = max(self.ans[rank], node.val)
            self.dfs(node.left, rank + 1)
            self.dfs(node.right, rank + 1)


        
        

        