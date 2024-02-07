class Solution {
public:
  string frequencySort(string s) {
    unordered_map<char, int> hm;
    map<int, string, greater<int>> ohm;
    string ans = "";
    
    for (auto& c: s) hm[c]++;
    
    for (auto& [key, value]: hm) { 
      ohm[value] += key; // altough this takes nlogn for each insertion we only need around 50 insertions no matter what the input is
    }
    
    for (auto& [key, value]: ohm) {
      for (auto& c: value) {
        for (int i = 0; i < key; i++) {
          ans += c;
        }
      }
    }
    
    return ans;
  }
};