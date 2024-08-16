class Solution {
public:
  vector<vector<int>> mergeSimilarItems(vector<vector<int>>& items1, vector<vector<int>>& items2) {
    map<int, int> hm;
    vector<vector<int>> ret;

    for (int i = 0; i < items1.size(); ++i) {
      hm[items1[i][0]] += items1[i][1];
    }
    for (int i = 0; i < items2.size(); ++i) {
      hm[items2[i][0]] += items2[i][1];
    }

    for (auto& e: hm) {
      ret.push_back({e.first, e.second});  
    }

    return ret;
  }
};