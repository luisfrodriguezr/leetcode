class Solution {
public:
  bool digitCount(string num) {
    map<char, int> hashMap;
    for (int i = 0; i < num.size(); i++) {
      hashMap[num.at(i)]++;
    }
    for (int i = 0; i < num.size(); i++) {
      int digit =  int(num.at(i) - '0');
      char hash = char(i + int('0'));
      if (hashMap[hash] != digit) return false;
    }
    return true;
  }
};