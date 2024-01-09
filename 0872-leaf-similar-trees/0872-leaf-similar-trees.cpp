/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
  bool leafSimilar(TreeNode* root1, TreeNode* root2) {
    vector<int> leafs1, leafs2;
    leaf_dfs(root1, leafs1);
    leaf_dfs(root2, leafs2);
    if (leafs1.size() != leafs2.size()) return false;
    
    for (int i = 0; i < leafs1.size(); i++) {
      if (leafs1[i] != leafs2[i]) return false;
    }
    
    return true;
  }
  void leaf_dfs(TreeNode* node, auto& leafs) {
    if (node->left == NULL and node->right == NULL) {
      leafs.push_back(node->val);
      return;
    }
    if (node->left != NULL) leaf_dfs(node->left, leafs);
    if (node->right != NULL) leaf_dfs(node->right, leafs);
  }
};