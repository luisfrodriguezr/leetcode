class Solution {
public:
  string makeFancyString(string s) {
    string res = "";
    if (s.size() < 3) return s;
    for (int i = 0; i < s.size(); i++) {
      if (i == 0 || i == s.size() - 1) {
        res += s[i]; continue;
      }
      else if (s[i - 1] == s[i] && s[i + 1] == s[i]) continue;
      res += s[i];
    }
    return res;
  }
};