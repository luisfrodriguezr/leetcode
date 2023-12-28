class Solution {
public:
  string reverseWords(string s) {
    string ans = s;
    int left = -1, window = 0;
    bool flag = false;
    for (int right = 0; right < s.size(); right++) {
      if (right + 1 == s.size()) flag = true;
      else if (s.at(right + 1) == ' ') flag = true;
      if (flag) {
        left++;
        window = left;
        while (left <= right) { // at max n computations; complexity O(1) amortized
          ans.at(right - (left - window)) = s.at(left);
          left++;
        }
        flag = false;
      }
    }
    return ans;
  }
};