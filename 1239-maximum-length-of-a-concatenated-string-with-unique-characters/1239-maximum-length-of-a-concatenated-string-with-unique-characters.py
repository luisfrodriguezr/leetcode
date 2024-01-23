class Solution:
    def maxLength(self, arr: List[str]) -> int:        
        return self.dfs(arr, 0, "")
    
    def dfs(self, arr: List[str], pos: int, res: str) -> int:        
        if len(res) != len(set(res)):
            return 0

        best = len(res)
        for i in range(pos, len(arr)):
            best = max(best, self.dfs(arr, i + 1, res + arr[i]))
        return best