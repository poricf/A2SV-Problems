class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int flip = 0, end = 0, start = 0,ans = 0;
        while(end < nums.size()){
            if(nums[end] == 0 ){
                flip++;
            }
            if(flip <= k){
                ans  = max(ans, end - start + 1);
            }

            while( flip > k){
                if(nums[start] == 0){
                    flip--;
                }
                start++;
            }
            end++;
        }
        return ans;

    }
};