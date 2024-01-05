class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    ans = 1
    sub = [nums[0],]
    for i in range(1, len(nums)):
      if sub[-1] < nums[i]:
        sub.append(nums[i])
        ans = max(ans, len(sub))
      else:
        for j in range(len(sub)):
          if sub[j] >= nums[i]:
            sub[j] = nums[i]
            break;

    return ans
