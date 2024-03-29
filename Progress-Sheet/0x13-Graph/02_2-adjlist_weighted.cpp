// for weighted adjacencylist representation is different we use pair
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;

    vector<vector<pair<int, int>>> adj(n + 1);

    for (int i = 0; i < m; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w}); // commnet this line For undirected graph
    }

    for (int i = 1; i <= n; i++)
    {
        cout << i << " --> { ";
        for (auto k : adj[i])
        {
            cout << "(" << k.first << ", " << k.second << "), ";
        }
        cout << "}" << endl;


    return 0;
}
/*
sample input 
5 6
1 3 -2
2 1 3
2 4 1
2 5 4
3 4 5
3 4 5
4 5 7

*/