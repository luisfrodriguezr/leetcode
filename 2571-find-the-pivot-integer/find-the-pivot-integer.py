class Solution:
  def pivotInteger(self, n: int) -> int:
    total_sum = n * (n + 1) / 2
    curr_sum = 0
    
    for num in range(1, n + 1):
      if curr_sum + num == total_sum - curr_sum: return num
      curr_sum += num
    
    return -1
        