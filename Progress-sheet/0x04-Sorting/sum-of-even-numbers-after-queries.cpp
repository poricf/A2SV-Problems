class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        int sz = queries.size();
        vector<int>result;
        for(int i = 0; i < sz; i++){
            nums[queries[i][1]] =  nums[queries[i][1]] + queries[i][0];
            int sum = 0;
            for(auto i : nums){
                if(i%2==0)sum+=i;

            }
            result.push_back(sum);
        }
    
        return result;
    }
};