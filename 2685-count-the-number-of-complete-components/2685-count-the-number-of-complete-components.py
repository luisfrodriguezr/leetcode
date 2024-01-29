class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
      rep = [x for x in range(n)]
      adj = [[0] * n for _ in range(n)]
      ans = 0
      hash_set = set(rep)
      def union(x , y):
        rep_x = find(x)
        rep_y = find(y)
        if rep_x != rep_y:
          rep[rep[y]] = rep_x
          hash_set.remove(rep_y)
          
      def find(n):
        if n == rep[n]:
          return n
        rep[n] = find(rep[n])
        return rep[n]
      
      for edge in edges:
        union(edge[0], edge[1])
        adj[edge[0]][edge[1]] = 1
        adj[edge[1]][edge[0]] = 1
      
      for s in hash_set:
        temp = 1
        for i in range(n):
          for j in range(i + 1, n):
            fi = find(i)
            fj = find(j)
            if find(i) == s and find(j) == s:
              if adj[i][j] == 0:
                temp = 0
        ans += temp
        
      return ans

        
        