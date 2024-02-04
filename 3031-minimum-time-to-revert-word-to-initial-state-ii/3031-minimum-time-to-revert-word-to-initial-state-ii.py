class Solution:
  def minimumTimeToInitialState(self, word: str, k: int) -> int:
    # find a valid prefix if found stop count and return ans
    for i in range(k, len(word), k): # count the number of times we need to remove k elements
      if word.startswith(word[i:]): return int(i / k)
    # if no valid prefix is found we need to recreate the whole word
    return ceil(len(word) / k)