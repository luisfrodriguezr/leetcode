class Solution {
public:
  int dietPlanPerformance(vector<int>& calories, int k, int lower, int upper) {
    int left = 0, right = 0, sum = 0, ans = 0, window;
    while (right < calories.size()) {
      sum += calories[right];
      window = right - left + 1;
      if (window > k) {
        sum -= calories[left];
        left++; window--;
      } 
      if (window == k) {
        if (sum < lower) ans--;
        if (sum > upper) ans++;
      }
      right++;
    }
    return ans;
  }
};