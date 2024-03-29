#include <bits/stdc++.h>
using namespace std;

/*
 * bfs - traverses graph in breadth-first order
 * @V: number of vertices of the graph
 * @adj: the graph represented as an adjacency list
 * Returns - traversed graph in the form of a list
 */
vector<int> bfs(int V, vector<int> adj[])
{
    vector<int> bfs_trav;
    vector<int> vis(V, 0); // Initialize all vertices as not visited

    vis[0] = 1; // Mark the starting vertex as visited
    queue<int> q;
    q.push(0);

    while (!q.empty())
    {
        int node = q.front();
        q.pop();
        bfs_trav.push_back(node);

        for (auto i : adj[node])
        {
            if (!vis[i])
            {
                vis[i] = 1; // Mark the adjacent vertex as visited
                q.push(i);
            }
        }
    }
     return (bfs_trav);
}


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

    vector<int> bfs_traversal = bfs(n, adj);

    cout << "BFS Traversal: ";
    for (int i = 0; i < bfs_traversal.size(); i++)
    {
        cout << bfs_traversal[i] << " ";
    }
    cout << endl;

    return 0;
}

/*
7 6
0 1
0 2
1 3
1 4
2 5
2 6
*/