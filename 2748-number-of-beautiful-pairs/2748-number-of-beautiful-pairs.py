class Solution:
  def countBeautifulPairs(self, nums: List[int]) -> int:
    def coprime(x, y):
      for i in range(2, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
          return False
      return True

    ans = 0
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        x = str(nums[i])[0]
        y = str(nums[j])[-1]
        if coprime(int(x), int(y)):
          ans += 1

    return ans