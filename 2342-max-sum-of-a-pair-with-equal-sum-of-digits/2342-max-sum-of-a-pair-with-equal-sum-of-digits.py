class Solution:
  def maximumSum(self, nums: List[int]) -> int:
    def sum_digits(n):
      ans = 0
      while n:
        ans += n % 10
        n = int(n/10)
      return ans
    
    # hash_map {hash_key = sum_digits(n): value = max(n, current_value)}
    hash_map = dict()
    ans = -1
    
    for num in nums:
      digits = sum_digits(num)
      if digits in hash_map:
        ans = max(ans, hash_map[digits] + num)
      hash_map[digits] = max(hash_map.get(digits, 0), num)
    
    return ans
      
        