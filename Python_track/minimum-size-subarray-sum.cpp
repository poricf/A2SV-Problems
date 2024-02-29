#define all(x) x.begin(),x.end()
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int N = nums.size();
        int r(0), l(0), res(INT_MAX),csum(0);

        while(r < N){
            csum += nums[r];
            while(csum >= target){
                res = min(res, r - l + 1);
                csum -= nums[l++];
            }
            r++;
        }
        return res < INT_MAX? res : 0;
    }
};