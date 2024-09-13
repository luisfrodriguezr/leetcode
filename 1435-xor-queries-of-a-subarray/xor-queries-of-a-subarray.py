class Solution:
  def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    ans = list()
    xor_arr = [0]

    for i in arr:
      xor_arr.append(xor_arr[-1] ^ i)

    for query in queries:
      ans.append(xor_arr[query[0]] ^ xor_arr[query[1] + 1])

    return ans

        