class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int k = p.size();
        vector<int> ans;

        vector<int> window(128);
        vector<int>  sample(128);
        for(int i = 0; i< p.size(); i++){
            sample[p[i]]++;
        }
        for (int i = 0,l=0; i < s.length();++i)
        {
            window[s[i]]++;
            if(i - l + 1 == k){
                if(window == sample) {
                    ans.push_back(l);
                }
                --window[s[l++]];
                
            }
        }
        //cba

        return ans;
    }
};