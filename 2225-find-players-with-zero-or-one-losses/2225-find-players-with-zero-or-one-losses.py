class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
      hashMap = dict()
      ans = [[], []]
      
      for match in matches:
        winner = match[0]
        losser = match[1]
        hashMap[winner] = hashMap.get(winner, 0)
        hashMap[losser] = hashMap.get(losser, 0) + 1
      
      for player, losses in hashMap.items():
        if losses == 0:
          ans[0].append(player)
        if losses == 1:
          ans[1].append(player)
      ans[0].sort()
      ans[1].sort()
      return ans;
        
        