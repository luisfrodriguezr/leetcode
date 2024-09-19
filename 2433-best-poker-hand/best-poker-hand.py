from collections import Counter
class Solution:
  def bestHand(self, ranks: List[int], suits: List[str]) -> str:
    ans = str()

    hm1 = dict(Counter(ranks))
    hm2 = dict(Counter(suits))

    if max(hm2.values()) == 5: ans = 'Flush'
    elif max(hm1.values()) >= 3: ans = "Three of a Kind"
    elif max(hm1.values()) == 2: ans = "Pair"
    else: ans = "High Card"

    return ans
        