class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
	int n = nums.size();
	vector<int> res(n);
	vector<pair<int, int>> num_index;
	for (int i=0; i<n; i++){
	    num_index.push_back(make_pair(nums[i], i));
	}
	sort(num_index.begin(), num_index.end());
	
	vector<int> vec_num;
	vector<int> vec_index;
	
	for (int i=0; i<n; i++){
        int index = num_index[i].second;
        int num = num_index[i].first;
        int next;
	    if (i + 1 == n){
		    next = num;
		    limit = -1;
	    } else {
            next = num_index[i + 1].first;
        }
        vec_num.push_back(num);
        vec_index.push_back(index);

	    if ((next - num) > limit){
            sort(vec_index.begin(), vec_index.end());
            for (int j = 0; j<vec_index.size(); j++){
                res[vec_index[j]] = vec_num[j];
            }
            vec_num.clear();
            vec_index.clear();
	    }
	}
	return res;
    }
};