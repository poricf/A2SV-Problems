class Solution {
private:
    void bfs(vector<vector<char>>& grid, int n, int m, vector<vector<int>>& vis, int row, int col) {
        vis[row][col] = 1;

        queue<pair<int, int>> q;
        q.push({row, col});

        while (!q.empty()) {
            int r = q.front().first;
            int c = q.front().second;
            q.pop();

            vector<pair<int, int>> directions{{-1, 0}, {1, 0}, {0, -1}, {0, 1}. {1, 1}};

            for (const auto& dir : directions) {
                int newRow = r + dir.first;
                int newCol = c + dir.second;

                if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < m &&
                    grid[newRow][newCol] == '1' && !vis[newRow][newCol]) {
                    vis[newRow][newCol] = 1;
                    q.push({newRow, newCol});
                }
            }
        }
    }

public:
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int cnt = 0;

        vector<vector<int>> vis(n, vector<int>(m, 0));

        for (int row = 0; row < n; row++) {
            for (int col = 0; col < m; col++) {
                if (grid[row][col] == '1' && !vis[row][col]) {
                    cnt++;
                    bfs(grid, n, m, vis, row, col);
                }
            }
        }

        return cnt;
    }
};