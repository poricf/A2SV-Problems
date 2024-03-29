#include <bits/stdc++.h>

using namespace std;

int main()
{
    int m,n,u,v;
    cin>>n>>m;

    vector<int> adj[n+1];
    memset(adj,0,sizeof(adj));

    for (int i = 1 ; i <=m; i++)
    {
        cin >> u >> v;//>> wt;
        adj[u].push_back(v); // wt;
        adj[v].push_back(u); // for undirected this will be commented 
    }
    
    for (int i = 1 ; i < n+1; i++)
    {
        cout << i << "--> { ";
        for (auto k : adj[i])
        {
            cout<<k<<", ";
        }
        cout<<"}"<<endl;
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