#include <iostream>
#include <vector>
using namespace std;

/*
 * DFS - one dfs traversal
 * @node - current node to be traversed
 * @adj - the graph in adjacency list
 * @vis - an array that indicates if current node is traversed or not
 * @ls - a list that containes the nodes that are visited
*/

void DFS(int node, vector<int> adj[], vector<int> &vis, vector<int> &ls)
{
    vis[node] = 1;
    ls.push_back(node);

    for(auto i : adj[node]){
        if(!vis[i])  DFS(i , adj , vis , ls);
    }

}
/*
 * dfs - traverses graph in Depth-first order // recursion
 * @V: number of vertices of the graph
 * @adj: the graph represented as an adjacency list
 * Returns - traversed graph in the form of a list
*/

vector<int> dfs(int V, vector<int> adj[])
{
    vector<int> vis(V, 0);
    vector<int> ls ;
    int start = 0; 
    
    DFS(start,adj, vis,ls);

    return (ls);
}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

int main()
{
    int n, m;
    cin >> n >> m;

    vector<int> adj[n];

    for (int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u); // For undirected graph
    }

    vector<int> dfs_traversal = dfs(n, adj);

    cout << "DFS Traversal: ";
    for (int i = 0; i < dfs_traversal.size(); i++)
    {
        cout << dfs_traversal[i] << " ";
    }
    cout << endl;

    return 0;
}

/*
6 7
0 1
0 2
1 3
1 4
2 4
3 4
3 5
*/