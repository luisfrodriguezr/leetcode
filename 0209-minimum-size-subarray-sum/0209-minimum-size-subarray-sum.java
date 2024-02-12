class Solution {
  public int minSubArrayLen(int target, int[] nums) {
    int left = 0, right = 0, curr = 0, ans = 100001;
    
    while (right < nums.length) {
      curr += nums[right];
      
      while (curr >= target) {
        ans = Math.min(ans, right - left + 1);
        curr -= nums[left];
        left++;
      }
      
      right++;
    }
    
    return ans != 100001 ? ans: 0;
  }
}