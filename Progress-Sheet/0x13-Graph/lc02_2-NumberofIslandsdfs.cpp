class Solution {
private:
    void dfs(vector<vector<char>> &grid, int m , int n, vector<vector<int>> &vis, int row, int col){
        vis[row][col] = 1;
        vector<pair<int, int>> dir{{0,1}, {0,-1}, {1,0}, {-1,0}};
        for (auto &d: dir){
            int nrow = row + d.first;
            int ncol = col + d.second;
        
            if (nrow >= 0 && nrow < n && ncol >= 0 && ncol < m  
            && grid[nrow][ncol] == '1' && !vis[nrow][ncol]){
                dfs(grid, m, n, vis, nrow, ncol);
                }
            }
    }
    
    
public:
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int cnt = 0;

        vector<vector<int>> vis(n, vector<int>(m,0));
        
        for (int row = 0; row < n ; row++)
        {
            for (int col = 0 ; col < m; col++)
            {
                if(grid[row][col] == '1' && !vis[row][col]){
                    cnt++;
                    dfs(grid, m, n, vis, row, col);
                }
            }
        }

        return cnt;
    }
};