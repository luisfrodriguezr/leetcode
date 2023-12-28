class Solution {
public:
  string reverseOnlyLetters(string s) {
    int right = s.size() - 1, left = 0;
    string ans = "";
    char c;
    
    while(left < s.size()) {
      c = s.at(left);
      if ((c >= 'a' && c <= 'z') || (c >= 'A' &&  c<= 'Z')) {
        c = s.at(right);
        while ((c < 'a' || c > 'z') && (c < 'A' || c > 'Z')) {
            right--;
            c = s.at(right);
        }
        ans += s[right];
        right--;
      } else {
        ans += s[left];
      }
      left++;
    }
    
    return ans;
  }
};