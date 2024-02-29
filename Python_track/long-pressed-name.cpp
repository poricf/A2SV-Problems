class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        int i = 0,j = 0, n, m;
        n = name.size();
        m = typed.size();
        if (m < n){
            return false;
        }
        while(i < n or j < m){
            int tcount = 0;
            int ncount = 0;
            if (name[i] == typed[j]){
                char curr = name[i];
                while(typed[j] == curr) tcount++,j++;
                while(name[i] == curr) ncount++,i++;
              

            }
            else{
                return false;
            }
            if (ncount > tcount){
                return false;
            }
        }
        return true;
    }
};