class Solution:
  def numSpecialEquivGroups(self, words: List[str]) -> int:
    ans = 0
    hm = dict()

    for word in words:
      key = str()

      tmp = list()
      for i in range(0, len(word), 2):
        tmp.append(word[i])
      tmp.sort()
      key += ''.join(tmp)

      tmp = list()
      for i in range(1, len(word), 2):
        tmp.append(word[i])
      tmp.sort()
      key += ''.join(tmp)

      hm[key] = hm.get(key, 0) + 1
    
    return len(hm)

      
  

        