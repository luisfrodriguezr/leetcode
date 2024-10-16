class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    ans = list()

    for i in range(numRows):
      ans.append([])
      for j in range(i):
        if j == 0: ans[i].append(1)
        else: ans[i].append(ans[i - 1][j - 1] + ans[i - 1][j])
      ans[i].append(1)
    
    return ans


        