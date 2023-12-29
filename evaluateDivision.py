class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Constructing the adjancey list
        adj = {}
        for i, eq in enumerate(equations):
            a,b = eq
            if a not in adj:
                adj[a] = [[b,values[i]]]
            else:   
                adj[a].append([b,values[i]])
            if b not in adj:
                adj[b] =[[a,1/values[i]]]
            else:
                adj[b].append([a,1/values[i]])
        visited = set()
        def dfs(src,target,visited):
            # Add the new element into vistied
            if src not in adj or target not in adj:
                return -1
            
            if src == target:
                return 1
            visited.add(src)
            for neighbour,weight in adj[src]:
                if neighbour not in visited:
                    result = dfs(neighbour,target,visited)
                    if result != -1:
                        return result * weight
            return -1.0

        res =[]
        for query in queries:
            res.append(dfs(query[0],query[1],set()))
        return res
    