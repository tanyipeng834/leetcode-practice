class UnionFind:
    def __init__(self, graph):
        self.parent = {}
        self.rank = {}
        # Create a set for each vertex
        for vertex in graph:
            self.parent[vertex] = vertex
            self.rank[vertex] = 0

        # Union operation based on the edges of the graph
        for vertex, neighbors in graph.items():
            for neighbor in neighbors:
                self.union(vertex, neighbor)


    def find(self,x):
        if self.parent[x] != x:
            # Path Compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y :
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] +=1





      
# Example graph represented as an adjacency list
graph_adjacency_list = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D']
}

# Create a UnionFind instance with the adjacency list
uf = UnionFind(graph_adjacency_list)
print(uf.find('A') == uf.find('B'))  # Should be True
print(uf.find('A') == uf.find('C'))  # Should be True
print(uf.find('A') == uf.find('D'))  # Should be True
print(uf.find('A') == uf.find('E')) 


