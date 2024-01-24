class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
      hash_map = dict()
      ans = 100001
      
      for i, card in enumerate(cards):
        if card in hash_map:
          ans = min(ans, i - hash_map[card] + 1)
        hash_map[card] = i
      if ans == 100001:
        ans = -1
      return ans
        