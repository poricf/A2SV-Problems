class Solution {
private:
    string converter(string s)
    {
        string res = "";
        for(auto &i : s){
            i = tolower(i);
        }

        for (auto i : s){
            if(isalnum(i)){
                res += i;
            }
        }
        return res;
    }
public:
    bool isPalindrome(string s) {
        string str = converter(s);
        int n = str.size(), j = n-1;
        
        for (auto i: str){
            if (j < n/2)
                break;
            if(i != str[j--])
                return false;
        }    
        return true;
    }
};