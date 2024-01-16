class Solution:
  def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
    # Explanation
    # taken_ones = min(k, numOnes)
    # taken_zeros = min(k - taken_ones, numZeros)
    # taken_negatives = k - taken_ones - taken_zeros
    # total_sum = taken_ones + 0*taken_zeros - taken_negatives
    # total_sum = taken_ones - taken_negatives
    return min(k, numOnes) - (k - min(k, numOnes) - min(k - min(k, numOnes), numZeros))
