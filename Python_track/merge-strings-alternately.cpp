class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string word3 = "";
        int i = 0, j = 0;

        while (i < word1.length() || j < word2.length()) {
            if (i < word1.length()) {
                word3 += word1[i++];
            }
            
            if (j < word2.length()) {
                word3 += word2[j++];
            }
        }
        
        return word3;
    }
};