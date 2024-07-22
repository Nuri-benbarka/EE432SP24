class Graph:
    def __init__(self, directed=False):
        self.num_of_node = 0
        self.adjacency_matrix = []
        self.directed = directed

    def add_node(self):
        self.num_of_node += 1
        for row in self.adjacency_matrix:
            row.append(0)
        zeros = [0 for _ in range(self.num_of_node)]
        self.adjacency_matrix.append(zeros)

    def add_edge(self, source, destination, wieght=1):
        if source > len(self.adjacency_matrix) or destination > len(self.adjacency_matrix):
            print("invalid source or destination")
            return
        self.adjacency_matrix[source][destination] = wieght
        if not self.directed:
            self.adjacency_matrix[destination][source] = wieght

    def remove_edge(self, source, destination):
        self.adjacency_matrix[source][destination] = 0
        if not self.directed:
            self.adjacency_matrix[destination][source] = 0

    def bfs(self, start):
        visited = [False for _ in range(self.num_of_node)]
        visited[start] = True
        ourqueue = [start]
        while ourqueue:
            current_v = ourqueue.pop(0)
            print(current_v, end=" ")
            for v, edge in enumerate(self.adjacency_matrix[current_v]):
                if edge > 0 and visited[v] is False:
                    ourqueue.append(v)
                    visited[v] = True

    def dfs(self, start):
        visited = [False for _ in range(self.num_of_node)]
        self._dfs(start, visited)

    def _dfs(self, v, visited):
        visited[v] = True
        print(v, end=" ")
        for nv, edge in enumerate(self.adjacency_matrix[v]):
            if edge > 0 and visited[nv] is False:
                self._dfs(nv, visited)


ourGraph = Graph()
ourGraph.add_node()
ourGraph.add_node()
ourGraph.add_node()
ourGraph.add_node()
ourGraph.add_node()
ourGraph.add_node()
ourGraph.add_node()
print(ourGraph.adjacency_matrix)

ourGraph.add_edge(0, 1)
ourGraph.add_edge(1, 2)
ourGraph.add_edge(2, 3)
ourGraph.add_edge(3, 4)
ourGraph.add_edge(4, 5)
ourGraph.add_edge(4, 6)
ourGraph.add_edge(6, 0)
ourGraph.add_edge(0, 5)
ourGraph.add_edge(5, 2)

print(ourGraph.adjacency_matrix)
print("BFS:")
ourGraph.bfs(0)
print(" ")
print("DFS:")
ourGraph.dfs(0)
print(" ")

ourGraph2 = Graph(directed=True)
ourGraph2.add_node()
ourGraph2.add_node()
ourGraph2.add_node()
ourGraph2.add_node()
ourGraph2.add_node()
ourGraph2.add_node()
ourGraph2.add_node()

ourGraph2.add_edge(1, 0, 2)
ourGraph2.add_edge(2, 1, 1)
ourGraph2.add_edge(2, 3, 6)
ourGraph2.add_edge(3, 4, 1)
ourGraph2.add_edge(4, 3, 3)
ourGraph2.add_edge(5, 4, 3)
ourGraph2.add_edge(6, 4, 4)
ourGraph2.add_edge(6, 0, 2)
ourGraph2.add_edge(5, 0, 1)
ourGraph2.add_edge(5, 2, 4)

print(ourGraph2.adjacency_matrix)

ourGraph2.remove_edge(3, 4)

print(ourGraph2.adjacency_matrix)
