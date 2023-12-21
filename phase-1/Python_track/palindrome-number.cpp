class Solution {
public:
    bool isPalindrome(int x) {
        string s = to_string(x);
        int n = s.length();
        int j = n-1;
        for (int i = 0; i < n/2; i++ )
        {
            if (s[i] != s[j--])
                return false;

        }
        return true;
    }
};