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
  int rangeSumBST(TreeNode* root, int low, int high) {
    return dfs(root, low, high);
  }
  
  int dfs(TreeNode* node, int low, int high) {
    if (node == NULL) return 0;
    int sum = 0;
    sum += dfs(node->left, low, high) + dfs(node->right, low, high); 
    if (node->val >= low && node->val <= high) return sum + node->val;
    else return sum;
  }
};