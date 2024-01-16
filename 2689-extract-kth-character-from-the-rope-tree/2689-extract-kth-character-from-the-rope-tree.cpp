/**
 * Definition for a rope tree node.
 * struct RopeTreeNode {
 *     int len;
 *     string val;
 *     RopeTreeNode *left;
 *     RopeTreeNode *right;
 *     RopeTreeNode() : len(0), val(""), left(nullptr), right(nullptr) {}
 *     RopeTreeNode(string s) : len(0), val(std::move(s)), left(nullptr), right(nullptr) {}
 *     RopeTreeNode(int x) : len(x), val(""), left(nullptr), right(nullptr) {}
 *     RopeTreeNode(int x, RopeTreeNode *left, RopeTreeNode *right) : len(x), val(""), left(left), right(right) {}
 * };
 */
class Solution {
public:
  char getKthCharacter(RopeTreeNode* root, int k) {
      string ans = dfs(root);
      return ans[k - 1];
  } 
  string dfs(RopeTreeNode* node) {
    if (node == NULL) return "";
    if (node->left == NULL && node->right == NULL) return node->val;
    return dfs(node->left) + dfs(node->right);
  }
};