class Solution {
public:
  bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
    int p1 = 0 , p2 = 0, i = 0, j = 0;
    while (i < word1.size() || j < word2.size()) {
      if (i >= word1.size() || j >= word2.size()) {
        return false;
      }
      if (word1[i].at(p1) != word2[j].at(p2)) {
        return false;
      }
      p1++; p2++;
      if (p1 == word1[i].size()){
        p1 = 0;
        i++;
      }
      if (p2 == word2[j].size()){
        p2 = 0;
        j++;
      }
    }
    return true;
  }
};