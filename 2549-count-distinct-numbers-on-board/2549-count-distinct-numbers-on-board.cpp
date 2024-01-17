class Solution {
public:
  int distinctIntegers(int n) {
    int ans = 0;
    queue<int> q;
    set<int> s;
    
    q.push(n);
    s.insert(n);
    while (!q.empty()) {
      for (int i = 1; i < q.front(); i++) {
        if (q.front() % i == 1) {
          q.push(i);
          s.insert(i);
        }
      }
      q.pop();
    }
    
    return s.size();
  }
};