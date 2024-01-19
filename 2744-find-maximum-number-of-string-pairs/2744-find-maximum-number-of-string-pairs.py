class Solution:
  def maximumNumberOfStringPairs(self, words: List[str]) -> int:
    hash_set = set()
    
    ans = 0
    for word in words:
      hash_key = tuple(sorted(word))
      if hash_key in hash_set:
        hash_set.remove(hash_key)
        ans += 1
      else:
        hash_set.add(hash_key)
    
    return ans 
        
      
        