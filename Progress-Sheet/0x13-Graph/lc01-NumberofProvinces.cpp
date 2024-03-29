class Solution {
private:
    void dfs(vector<int>* adjLs, vector<int>& vis, int node) {
        vis[node] = 1;
        for (auto it : adjLs[node]) {
            if (!vis[it]) {
                dfs(adjLs, vis, it);
            }
        }
    }
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<int>* adjLs = new vector<int>[n];

        // Change adjmatrix to list
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (isConnected[i][j] == 1 && i != j) {
                    adjLs[i].push_back(j);
                    adjLs[j].push_back(i);
                }
            }
        }

        vector<int> vis(n, 0);
        int cnt = 0;

        for (int it = 0; it < n; it++) {
            if (vis[it] == 0) {
                cnt++;
                dfs(adjLs, vis, it);
            }
        }

        

        return cnt;
    }
};