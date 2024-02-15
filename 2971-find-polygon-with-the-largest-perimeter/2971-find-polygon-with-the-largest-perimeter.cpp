class Solution {
public:
  long long largestPerimeter(vector<int>& nums) {
    int k = nums.size(), i = 0;
    long long perimeter = 0;
    sort(rbegin(nums), rend(nums));
    for (int num: nums) perimeter += num;
    while (perimeter - nums[i] <= nums[i]) {
      perimeter -= nums[i];
      k--; i++;
      if (i == nums.size()) break;
    }
    if (k < 3) return -1;
    return perimeter;
  }
};