class Solution {
public:
  bool areOccurrencesEqual(string s) {
    int hashMap[26] = {};
    for (char c: s) {
      hashMap[c - 'a']++;
    }
    int freq = hashMap[s[0] - 'a'];
    for (char c: s) {
      if (hashMap[c - 'a'] != freq) return false;
    }
    return true;
  }
};