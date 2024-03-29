class Solution {
  private:
    bool detect(int start, int parent, int vis[], vector<int> adj[])
    {
        vis[start] = 1;
        
        for (auto i : adj[start])
        {
            if(!vis[i]) {
                if(detect(i,start,vis,adj)== true)
                    return true;
            }
            else if (i != parent)
                return true;
        }
        
        return false;
        
    }
  public:
    // Function to detect cycle in an undirected graph.
    bool isCycle(int V, vector<int> adj[]) {
        int vis[V] = {0};
        for (int i = 0; i < V; i++)
        {
            if(!vis[i])
            {
                if(detect(i,-1,vis,adj) == true)
                    return true;
            }
        }
        
        return false;
    }
};
