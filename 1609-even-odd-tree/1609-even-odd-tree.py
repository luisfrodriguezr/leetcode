class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        prev = []

        def dfs(current: TreeNode, level: int) -> bool:
            if current is None:
                return True

            if current.val % 2 == level % 2:
                return False

            while(len(prev) <= level):
                prev.append(0)
            if prev[level] != 0 and \
                    ((level % 2 == 0 and current.val <= prev[level]) or \
                     (level % 2 == 1 and current.val >= prev[level])):
                return False

            prev[level] = current.val

            return dfs(current.left, level + 1) and dfs(current.right, level + 1)
        
        current = root
        return dfs(current, 0)
