class Solution {
public:
  vector<vector<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
    map<int, vector<pair<int, int>>> hm;
    vector<vector<int>> ans;
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        hm[abs(i - rCenter) + abs(j - cCenter)].push_back(make_pair(i, j));
      }
    }
    for (auto& [k, v]: hm) {
      for (auto& [i, j]: v) {
        ans.push_back({i, j});
      }
    }
    return ans;
  }
};