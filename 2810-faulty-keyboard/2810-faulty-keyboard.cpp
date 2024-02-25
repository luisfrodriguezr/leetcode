class Solution {
public:
  string finalString(string s) {
    string ans = "";

    for (int i = 0; i < s.size(); ++i) {
      if (s[i] == 'i') {
        reverse(begin(s), begin(s) + i);
        s = s.substr(0, i) + s.substr(i + 1, s.size() - i);
        i--;
      }
    }
    
    return s;
  }
};