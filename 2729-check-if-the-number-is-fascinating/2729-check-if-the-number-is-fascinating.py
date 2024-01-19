class Solution:
  def isFascinating(self, n: int) -> bool:
    num = str(n) + str(n * 2) + str(n * 3)
    hash_map = dict()
    
    for digit in num:
      hash_map[digit] = hash_map.get(digit, 0) + 1

    for i in range(1, 10):
      if hash_map.get(str(i), 0) != 1:
        return False
    
    return True
    
    
        