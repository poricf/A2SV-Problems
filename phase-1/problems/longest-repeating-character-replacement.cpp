class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char,int> window;
        
        int l = 0, r = 0;
        int maxfreq(0), res(0);

        while( r < s.length())
        {
            maxfreq = max(maxfreq,++window[s[r]]);
            while(((r - l + 1) - maxfreq) > k) --window[s[l++]];
            res = max(res, r - l + 1);
            r++;
        }
        return res;
    }
};