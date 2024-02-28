#define all(x) x.begin(),x.end()
class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(all(people));
        for(auto i : people) cout<<i<<" ";

        int res= people.size();
        int end = res - 1;
        int start = 0;

        while(start < end){
            int sum = people[end--];
            if(sum + people[start] <= limit){
                res--;
                sum += people[start++];

                }
            
        }
        return res;
    }
};