class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
      last = ans = longest = 0

      for log in logs:
        time = log[1] - last
        
        if time > longest:
          longest = time
          ans = log[0]
        if time == longest:
          ans = min(ans, log[0])
        
        last = log[1]
      
      return ans
        
        