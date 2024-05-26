class Solution:
  def trimMean(self, arr: List[int]) -> float:
    n = len(arr) // 20
    arr = sorted(arr)
    s = 0
    
    for i in range(n, len(arr) - n):
      s += arr[i]

    return s / (len(arr) -  n * 2)