class Solution {
public:
  int minimumAddedCoins(vector<int>& coins, int target) {
    sort(begin(coins), end(coins));
    int max = 0;
    int res = 0;
    int i = 0;
    while (i < coins.size()) {
      if (coins[i] <= (max + 1)) {
        max += coins[i];
        i++;
      } else {
        max += max + 1;
        res++;
      }
      if (max >= target) break;
    }
    while (max < target) {
        max += max + 1;
        res++;
    }
    return res;
  }
};