from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root, v, d):
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root

        queue = deque([root])
        depth = 1

        while depth < d - 1:
            temp = deque()
            while queue:
                node = queue.popleft()
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            depth += 1

        while queue:
            node = queue.popleft()
            temp = node.left
            node.left = TreeNode(v)
            node.left.left = temp
            temp = node.right
            node.right = TreeNode(v)
            node.right.right = temp

        return root
 