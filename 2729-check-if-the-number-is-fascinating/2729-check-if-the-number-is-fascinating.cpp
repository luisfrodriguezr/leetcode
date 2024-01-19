class Solution {
public:
  bool isFascinating(int n) {
    unordered_map<char, int> hash_map;
    string num = to_string(n) + to_string(n * 2) + to_string(n * 3);
    
    for (auto& c: num) hash_map[c]++;
    
    for (int i = 1; i < 10; i++) 
      if (hash_map['0' + i] != 1)
        return false;
    
    return true;
  }
};