class Solution:
  def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    hm = dict()
    ans = list()

    for word in s1.split(' '):
      hm[word] = hm.get(word, 0) + 1

    for word in s2.split(' '):
      hm[word] = hm.get(word, 0) + 1

    for k, v in hm.items():
      if v == 1: ans.append(k)

    return ans
        