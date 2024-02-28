#define all(x) x.begin(),x.end()
class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        sort(all(skill));
        int n = skill.size();
        int start = 0 , end = n - 1;
        if(n==2) 
            return skill[0]*skill[1];
        
        long long sample =  skill[start] + skill[end];
        long long res = skill[start++] * skill[end--] ;
        while(start < end){
            if(skill[start] + skill[end] == sample){
                res += (skill[start++]*skill[end--]);
                cout<<res;
            }
            else
                return -1;
        }

        return res;
    }
};