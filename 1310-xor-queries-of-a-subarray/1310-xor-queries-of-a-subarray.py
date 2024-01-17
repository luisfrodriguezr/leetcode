class Solution:
  def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    prefix = [arr[0]]
    for i in range(1, len(arr)):
      prefix.append(prefix[i - 1] ^ arr[i])
    
    ans = []
    for query in queries:
      ans.append(prefix[query[1]] ^ prefix[query[0]] ^ arr[query[0]])
    
    return ans