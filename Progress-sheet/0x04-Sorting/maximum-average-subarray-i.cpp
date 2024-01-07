using namespace std;
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        
        
        double sum = 0;
        for (int i = 0; i < k ; i++)
        {
             sum += nums[i];
        }
        int i = 0, j = k;
        double maxav = sum/k;

        while ( j < nums.size()){
            sum -= nums[i++];
            sum += nums[j++];

            maxav = max(maxav, sum/k);
        }

        return maxav;
        


    }
};