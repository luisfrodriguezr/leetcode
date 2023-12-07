class Solution {
public:
  int countCharacters(vector<string>& words, string chars) {
    int ans = 0;
    map<char, int> hashMap;
    for (string word: words) {
      for (char c: chars) {
        hashMap[c]=0;
      }
      for (char c: chars) {
        hashMap[c]++;
      }
      bool is_good = true;
      for (char c: word) {
        if (hashMap[c] > 0) {
          hashMap[c]--;
        } else {
          is_good = false;
          break;
        }
      }
      if (is_good) {
        ans += word.size();
      }
    }
    return ans;
  }
};