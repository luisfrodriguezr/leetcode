class Solution:
  def generatePossibleNextMoves(self, currentState: str) -> List[str]:
    ans = []
    s = [*currentState]
    for i in range(len(s) - 1):
      if currentState[i: i + 2] == '++':
        new_s = [*currentState]
        new_s[i] = '-'
        new_s[i + 1] = '-'
        ans.append(''.join(new_s))
    return ans;