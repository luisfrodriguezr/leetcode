class Solution {
public:
  int maximumNumberOfStringPairs(vector<string>& words) {
    unordered_set<string> hash_set;
    
    int ans = 0;
    for (auto& word: words) {
      sort(begin(word), end(word));
      if (hash_set.find(word) != end(hash_set) ) {
        hash_set.erase(word);
        ans++;
      } else {
        hash_set.insert(word);
      }
    }
    
    return ans;
  }
};