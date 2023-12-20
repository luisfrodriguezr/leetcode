class Solution {
public:
  vector<vector<int>> largeGroupPositions(string s) {
    int start = 0, end = 0, count = 0;
    vector<vector<int>> ans;
    for (int i = 1; i < s.size(); i++) {
      if (s.at(i - 1) == s.at(i)) {
        if (count == 0){
          count = 2;
          start = i - 1;
          
        } else {
          count++;
        }
        end = i;
      } else {
        if (count >= 3) ans.push_back({start, end});
        count = 0;
      }
    }
    if (count >= 3) ans.push_back({start, end});
    return ans;
  }
};