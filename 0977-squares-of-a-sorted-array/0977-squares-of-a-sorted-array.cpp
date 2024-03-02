// Time complexity O(n)
// Space complexity O(n) when considering the output
class Solution {
public:
  vector<int> sortedSquares(vector<int>& nums) {
    // part I set up two pointers 
    // we can achieve this by looking at the point when a positive number appears; time cost (~n/2)
    int i = 0;
    int j = 0;
    while (nums[i] < 0) { // find the first non-negative number
      i++;
      if (i == nums.size()) break;
    }
    j = i - 1;

    // part II loop both set of numbers (negatives/positives) and add them to the answer keeping the non-decreasing order; time cost (~n/2)
    vector<int> ans;
    while (j >= 0 && i < nums.size()) {
      int first_square = nums[i] * nums[i];
      int second_square = nums[j] * nums[j];
      if (first_square < second_square) {
        ans.push_back(first_square);
        i++;
      } else {
        ans.push_back(second_square);
        j--;
      }
    }

    // part III loop remainder negative numbers; time cost (~n/2)
    while (j >= 0) {
      ans.push_back(nums[j] * nums[j]);
      j--;
    }

    // part IV loop remainder positive numbers; time cost(~n/2)
    while (i < nums.size()) {
      ans.push_back(nums[i] * nums[i]);
      i++;
    }
    return ans;
    // total cost 4 * n/2
    // 2n worst case scenario (considering all nums negatives)
  }
};