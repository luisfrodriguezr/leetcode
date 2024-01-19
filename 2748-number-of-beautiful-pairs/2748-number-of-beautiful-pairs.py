class Solution:
  def countBeautifulPairs(self, nums: List[int]) -> int:
    ans = 0
    digits = [0] * 10
    for i in range(len(nums)):
        x = str(nums[i])[-1]
        f = str(nums[i])[0]
        for y in range(1, len(digits)):
          if digits[y]:
            if (math.gcd(y, int(x)) == 1): ans += digits[y]
        digits[int(f)] += 1
    return ans