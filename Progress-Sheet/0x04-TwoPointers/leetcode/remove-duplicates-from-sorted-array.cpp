#define all(v) v.begin(), v.end()
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        nums.erase(unique(all(nums)),nums.end());
        int k=nums.size();
        return(k);
        
    }
};