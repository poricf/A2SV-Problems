#include <iostream>
#include <vector>
#include <stack>
using namespace std;
/**
 * DFS Traversal using an Explicit Stack
 *
 * This code performs a Depth-First Search (DFS) traversal on a graph represented
 * as an adjacency list using an explicit stack. The code visits each node in the
 * graph and outputs the order of traversal.
 *
 * Function:
 * vector<int> dfs(int node, vector<int> adj[], vector<int>& vis, vector<int>& ls)
 *
 * Parameters:
 * - node: The current node to be traversed.
 * - adj: The graph represented as an adjacency list.
 * - vis: An array that indicates whether a node is visited or not.
 * - ls: A list that contains the nodes visited during the traversal.
 *
 * Returns:
 * The list of nodes visited during the DFS traversal.
 *
 * Algorithm:
 * 1. Create an empty stack and push the starting node onto the stack.
 * 2. Mark the starting node as visited.
 * 3. While the stack is not empty:
 *    3.1 Pop the top node from the stack and add it to the visited list.
 *    3.2 Traverse the adjacent nodes of the current node.
 *        - If an adjacent node is not visited, push it onto the stack and mark it as visited.
 * 4. Return the visited list containing the DFS traversal order.
 *
 * Main Function:
 * int main()
 *
 * - Reads the number of nodes (n) and edges (m) in the graph.
 * - Creates an adjacency list representation of the graph.
 * - Initializes the visited array and the DFS traversal list.
 * - Calls the dfs() function to perform the DFS traversal.
 * - Prints the DFS traversal order.
 *
 * Example Usage:
 * Input:
 *   6 7      // Number of nodes (6) and edges (7)
 *   0 1      // Edge from node 0 to node 1
 *   0 2      // Edge from node 0 to node 2
 *   1 3      // Edge from node 1 to node 3
 *   1 4      // Edge from node 1 to node 4
 *   2 3      // Edge from node 2 to node 3
 *   2 5      // Edge from node 2 to node 5
 *   3 4      // Edge from node 3 to node 4
 *
 * Output:
 *   DFS Traversal: 0 2 5 3 4 1
 */

vector<int> dfs(int V, vector<int> adj[])
{
    vector<int> vis(V, 0);
    vector<int> ls;
    stack<int> st;

    st.push(0);git 
    vis[0] = 1;

    while (!st.empty()) {
        int node = st.top();
        st.pop();
        ls.push_back(node);

        for (auto i : adj[node]) {
            if (!vis[i]) {
                st.push(i);
                vis[i] = 1;
            }
        }
    }

    return ls;
}

int main()
{
    int n, m;
    cin >> n >> m;

    vector<int> adj[n];

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u); // For undirected graph
    }

    vector<int> dfs_traversal = dfs(n, adj);

    cout << "DFS Traversal: ";
    for (int i = 0; i < dfs_traversal.size(); i++) {
        cout << dfs_traversal[i] << " ";
    }
    cout << endl;

    return 0;
}