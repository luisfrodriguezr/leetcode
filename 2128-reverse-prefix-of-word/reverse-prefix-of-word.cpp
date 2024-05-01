class Solution {
public:
  string reversePrefix(string word, char ch) {
    int j = 0;
    for (int i = 0; i < word.size(); i++) {
      if (word[i] == ch) {
        j = i;
        break;
      }
    }
    char aux;
    int i = 0;
    while (i < j) {
      aux = word[i];
      word[i] = word[j];
      word[j] = aux;
      i++; j--;
    }
    return word;
  }
};;