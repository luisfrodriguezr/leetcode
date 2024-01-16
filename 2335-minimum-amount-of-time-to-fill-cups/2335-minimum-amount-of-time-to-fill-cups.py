class Solution:
  def fillCups(self, amount: List[int]) -> int:
    return max(max(amount), sum(amount) // 2 + sum(amount) % 2)
      
        