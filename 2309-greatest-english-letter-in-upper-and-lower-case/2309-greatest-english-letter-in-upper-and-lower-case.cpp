// Time O(n)
// Space O(n)
class Solution {
public:
  string greatestLetter(string s) {
    bool lower[26] = {}, upper[26] = {};
    int hash;
    string ans = "";
    for (char c: s) {
      if (c >= 'a') {
        hash = c - 'a';
        lower[hash] = true;
      } else {
        hash = c - 'A';
        upper[hash] = true;
      }
    }
    for (int i = 25; i >= 0; i--) {
      if (lower[i] && upper[i]) {
        ans += char(int('A') + i);
        return ans;
      }
    }
    return ans;
  }
};