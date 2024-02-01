class Solution:
  def numOfPairs(self, nums: List[str], target: str) -> int:
    hash_map = dict()
    ans = 0
    
    for num in nums:
      substr1 = target[:-len(num)]
      if substr1 in hash_map and substr1 + num == target:  
        ans += hash_map[substr1]
      
      substr2 = target[len(num):]
      if substr2 in hash_map and num + substr2 == target:  
        ans += hash_map[substr2]
       
      hash_map[num] = hash_map.get(num, 0) + 1
      
      
    return ans
      
        