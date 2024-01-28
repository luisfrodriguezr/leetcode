class Solution:
  def maxScoreIndices(self, nums: List[int]) -> List[int]:
    prefix_0 = [0]
    prefix_1 = [0]
    for i in range(len(nums)):
      prefix_0.append(prefix_0[-1] + (1 - int(nums[i])))
      prefix_1.append(prefix_1[-1] + (int(nums[i])))
    m = -1
    scores = []
    for i in range(1, len(nums) + 2):
      score = prefix_0[i - 1]
      score += prefix_1[-1] - prefix_1[i - 1] 
      scores.append(score)
      m = max(m, score)
    ans = []
    for i, score in enumerate(scores):
      if score == m:
        ans.append(i)
    
    return ans
      