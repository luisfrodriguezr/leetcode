class Solution {
public:
  int canBeTypedWords(string text, string brokenLetters) {
    int hashMap[26] = {0};
    int ans = 0;
    for (char c: brokenLetters) {
      ++hashMap[c - 'a'];
    }
    bool word_not_broken = true;
    for (int i = 0; i < text.size(); i++) {
      char c = text.at(i);
      if (c != ' ') {
        if (hashMap[c - 'a']) word_not_broken = false;
      }
      if (c == ' ' || i == text.size() - 1) {
        if (word_not_broken) ++ans;
        word_not_broken = true;
        continue;
      }
    }
    return ans;
  }
};