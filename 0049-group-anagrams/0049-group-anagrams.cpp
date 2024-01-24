class Solution {
public:
  vector<vector<string>> groupAnagrams(vector<string>& strs) {
    vector<vector<string>> ans;
    unordered_map<string, vector<string>> hash_map;
    string hash_key;
    
    for (auto& str: strs) {
      hash_key = str;
      sort(begin(hash_key), end(hash_key));
      hash_map[hash_key].push_back(str);
    }
    
    for (auto& [hash_keys, strings]: hash_map) {
      ans.push_back(strings);
    }
    
    return ans;
  }
};