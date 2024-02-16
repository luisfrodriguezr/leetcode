class Solution {
public:
  int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
    unordered_map<int, int> hash_map;
    vector<int> freqs;
    int ans;
    
    for (int& num: arr) hash_map[num]++;
    
    for (auto& [_, freq]: hash_map) freqs.push_back(freq);
    
    sort(begin(freqs), end(freqs));
    
    ans = freqs.size();
    for (auto& freq: freqs) {
      if (k - freq >= 0) {
        k -= freq;
        ans--;
      }
      else break;
    }
    
    return ans;
  }
};