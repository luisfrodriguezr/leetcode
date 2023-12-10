class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int count = 0;
        int m = *std::max_element(nums.begin(), nums.end());
        long long res = 0;
        int p = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == m) {
                count++;
            }
            while (count >= k) {
                res += (nums.size() - i);
                if (nums[p++] == m) {
                    count--;
                }
            }
        }
        return res;
    }
};