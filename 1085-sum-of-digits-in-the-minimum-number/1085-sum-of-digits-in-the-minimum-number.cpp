class Solution {
public:
    int sumOfDigits(vector<int>& nums) {
      int ans = 0;
      int num = *min_element(begin(nums), end(nums));
      while(num){
        ans += num % 10;
        num /= 10;
      }
      return 1 - ans % 2;
    }
};