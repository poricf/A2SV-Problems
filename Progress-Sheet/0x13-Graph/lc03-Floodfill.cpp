class Solution {
private: 
    vector<vector<int>> bfs(vector<vector<int>>& image, int sr, int sc, int color,int m, int n){
        int value = image[sr][sc];
        image[sr][sc] = color;

        queue<pair<int , int>> q;

        q.push({sr,sc});

        vector<pair<int, int>> dir{{1,0}, {0,1}, {0, -1}, {-1, 0}}; 
        while (!q.empty())
        {
            int sr = q.front().first;
            int sc = q.front().second;
            q.pop();
            for (const auto &d : dir)
            {
                int nrow  = sr + d.first;
                int ncol =  sc + d.second;

                if (nrow >=0 && nrow < n && ncol >=0 && ncol < m && 
        image[nrow][ncol] != color && image[nrow][ncol] == value)
                {
                    image[nrow][ncol] = color;
                    q.push({nrow,ncol});
                    
                }
            }
        }
class Solution {
private: 
    vector<vector<int>> bfs(vector<vector<int>>& image, int sr, int sc, int color,int m, int n){
        int value = image[sr][sc];
        image[sr][sc] = color;

        queue<pair<int , int>> q;

        q.push({sr,sc});

        vector<pair<int, int>> dir{{1,0}, {0,1}, {0, -1}, {-1, 0}}; 
        while (!q.empty())
        {
            int sr = q.front().first;
            int sc = q.front().second;
            q.pop();
            for (const auto &d : dir)
            {
                int nrow  = sr + d.first;
                int ncol =  sc + d.second;

                if (nrow >=0 && nrow < n && ncol >=0 && ncol < m && 
        image[nrow][ncol] != color && image[nrow][ncol] == value)
                {
                    image[nrow][ncol] = color;
                    q.push({nrow,ncol});
                    
                }
            }
        }

        return image;
    }
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {

        int m = image[0].size();
        int n = image.size();

        vector<vector<int>> initImage;
        initImage = image;
        image = bfs(image,sr,sc,color,m,n);

        return image;

    }
};
        return image;
    }
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {

        int m = image[0].size();
        int n = image.size();

        vector<vector<int>> initImage;
        initImage = image;
        image = bfs(image,sr,sc,color,m,n);

        return image;

    }
};