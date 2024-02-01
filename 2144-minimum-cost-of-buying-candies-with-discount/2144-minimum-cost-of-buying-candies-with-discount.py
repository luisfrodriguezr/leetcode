class Solution:
  def minimumCost(self, cost: List[int]) -> int:
    cost.sort(reverse=True)
    ans = 0
    i = 0
    j = 1
    while i + 1 < len(cost) and j + 1 < len(cost):
      k = j + 1
      while k < len(cost):
        if min(cost[i], cost[j]) >= cost[k]:
          ans += cost[i] + cost[j]
          cost[i] = 0
          cost[j] = 0
          cost[k] = 0
          break
        k += 1
      i = j + 1
      while i < len(cost):
        if cost[i] != 0: break
        i += 1
      j = i + 1
      while j < len(cost):
        if cost[j] != 0: break
        j += 1
    ans += sum(cost)
    return ans
      
    
        