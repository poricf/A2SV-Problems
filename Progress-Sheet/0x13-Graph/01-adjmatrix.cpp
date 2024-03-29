#include <bits/stdc++.h>

using namespace std;

int main()
{
    int m,n,u,v;
    cin>>n>>m;

    int adj[n+1][n+1];
    memset(adj,0,sizeof(adj));

    for (int i = 1 ; i <= m; i++)
    {
        cin >> u >> v;//>> wt;
        adj[u][v] = 1; // wt;
        adj[v][u] = 1; // for undirected this will be commented 
    }

    for (int i = 1 ; i < n+1; i++)
    {
        for (int j = 0 ; j < n+1 ; j++)
        cout << adj[i][j] << " ";
        cout << endl; 
    }

    
}

/*
sample input  
5 6
2 1
1 3
2 4
2 5
3 4
4 5
*/