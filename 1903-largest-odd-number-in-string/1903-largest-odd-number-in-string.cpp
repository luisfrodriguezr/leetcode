class Solution {
public:
  string largestOddNumber(string num) {
    int n = num.size();
    for (int i = n - 1; i >= 0; i--) {
      if (num.at(i) % 2) { // If digit is odd then
        // Return the substr from the beginning to this number
        return num.substr(0, i + 1);
      }
    }
    // Return empty string if there is no odd number
    return "";
  }
};