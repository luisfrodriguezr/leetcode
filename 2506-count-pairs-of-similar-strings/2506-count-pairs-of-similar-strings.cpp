class Solution {
public:
  int similarPairs(vector<string>& words) {
    unordered_map<int, int> hash_map;
    int key, ans = 0;
    
    for (int i = 0; i < words.size(); ++i) {
      key = 0;
      for (int k = 0; k < words[i].size(); k++) {
        key |= 1 << (words[i][k] - 'a');
      }
      hash_map[key]++;
      ans += (hash_map[key] - 1);
    }
    
    return ans;
  }
};