'''
https://leetcode.com/problems/critical-connections-in-a-network/
1192. Critical Connections in a Network
Hard

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

 

Constraints:

    1 <= n <= 10^5
    n-1 <= connections.length <= 10^5
    connections[i][0] != connections[i][1]
    There are no repeated connections.
'''
class Solution:
    from collections import defaultdict
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        dfs_level = {}
        lowest_conn = {}
                
        def dfs(node, parent, level):
            if node in dfs_level:
                return
            
            dfs_level[node] = level
            lowest_conn[node] = level
            
            for neighbor in graph[node]:
                if neighbor not in dfs_level:
                    dfs(neighbor, node, level + 1)
            
            neighbor_lows = []
            for neighbor in graph[node]:
                if neighbor != parent:
                    neighbor_lows.append(lowest_conn[neighbor])
            
            lowest_conn[node] = min([dfs_level[node]] + neighbor_lows)     
            
        dfs(0, None, 0)
        
        output = []
        for u, v in connections:
            if lowest_conn[u] > dfs_level[v] or lowest_conn[v] > dfs_level[u]:
                output.append([u,v])
        
        return output