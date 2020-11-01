class Graph:
    def __init__(self, v):
        self.V = v
        self.adj = [[] for _ in range(v)]
        self.dfsStr = ""
        self.bfsStr = ""

    def addEdge(self, s, e):
        self.adj[s].append(e)

    def DFS(self, s):
        visited = [False for _ in range(self.V)]
        self.dfsStr += str(s) + " "

        for next in self.adj[s]:
            if not visited[next]:
                visited[next] = True
                self.DFS(next)

    def BFS(self, s):
        visited = [False for _ in range(self.V)]
        queue = []

        visited[s] = True
        queue.append(s)

        while queue:
            s = queue.pop(0)
            self.bfsStr += str(s) + " "

            for next in self.adj[s]:
                if not visited[next]:
                    visited[next] = True
                    queue.append(next)


V, E = map(int, input().split())
g = Graph(V)
for _ in range(E):
    edge = [int(x) for x in input().split()]
    g.addEdge(edge[0], edge[1])

g.BFS(0)
g.DFS(0)
print("DFS : [{}]".format(g.dfsStr))
print("BFS : [{}]".format(g.bfsStr))

