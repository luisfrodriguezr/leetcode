class Solution {
public:
  bool isCovered(vector<vector<int>>& ranges, int left, int right) {
    set<int> numbers;
    for (int i = left; i <= right; i++) {
      numbers.insert(i);
    }
    for (auto& range: ranges) {
      for (int i = range[0]; i <= range[1]; i++) {
        numbers.erase(i);
        if (numbers.empty()) return true;
      }
    }
    return false;
  }
};