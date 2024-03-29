class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int vis[n][m];
        queue<pair< pair<int,int> ,int >> q;
        int freshCount = 0;
        vector<pair<int,int>> dir{{0,1}, {0,-1}, {1,0}, {-1,0}};

        for (int i = 0; i < n; i++)
        {
            for (int j = 0 ; j < m; j++)
            {
                if (grid[i][j] == 1) 
                    freshCount++, vis[i][j] = 1;
                else if (grid[i][j] == 2)
                  q.push({{i, j}, 0}), vis[i][j] = 2;
                else                 
                    vis[i][j] = 0;
             }
        }
        int tm = 0;
        int rotFresh = 0;
        while(!q.empty())
        {
            int row = q.front().first.first;
            int col = q.front().first.second;
            int t = q.front().second;
            
            tm = max(t,tm);
            q.pop();
            for (const auto &d : dir){
                int nrow = row + d.first;
                int ncol = col + d.second;
                
                if(nrow >= 0 && nrow < n && ncol >=0 && ncol < m
                  && grid[nrow][ncol] == 1 && vis[nrow][ncol] != 2 ){
                      q.push({{nrow,ncol},t+1});
                      vis[nrow][ncol] = 2;
                      rotFresh++;
                  }
            }
        }

        if(freshCount > rotFresh)  
            return -1;

        return tm;
    }
};
