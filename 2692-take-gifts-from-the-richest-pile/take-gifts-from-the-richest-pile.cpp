class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        int n;
        priority_queue<pair<long long, int>> pq;
        long long ans = 0;

        for (int i = 0; i < gifts.size(); i++) {
          pq.push(make_pair(gifts[i], i));
        }

        while(k--) {
          auto e = pq.top();
          pq.pop();
          n = floor(sqrt(e.first));
          gifts[e.second] = n;
          pq.push(make_pair(n, e.second));
        }

        for (auto gift: gifts) {
          ans += gift;
        }

        return ans;
    }
};