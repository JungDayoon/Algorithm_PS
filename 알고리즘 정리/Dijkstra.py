import heapq

INF = 999999


class Graph:
    def __init__(self, v):
        self.heap = []
        self.parent = [-1 for _ in range(v)]
        self.V = v
        self.adj = [[] for _ in range(v)]
        self.dist = [INF for _ in range(v)]

    def addEdge(self, s, e, w):
        self.adj[s].append([e, w])

    def dijkstra(self, s):
        self.dist[s] = 0
        visited = [False for _ in range(self.V)]

        heapq.heappush(self.heap, (self.dist[s], [s, self.dist[s], -1]))

        while self.heap:
            head_num, head_dist, head_parent = heapq.heappop(self.heap)[1]
            # if head[1] > self.dist[head[0]]:
            #     continue
            if visited[head_num]:
                continue
            visited[head_num] = True

            for next in self.adj[head_num]:
                if head_dist + next[1] < self.dist[next[0]]:
                    self.dist[next[0]] = head_dist + next[1]
                    self.parent[next[0]] = head_num
                    heapq.heappush(self.heap, (self.dist[next[0]], [next[0], self.dist[next[0]], head_num]))

    def findPath(self, s, arr):
        arr.append(str(s))

        if self.parent[s] == -1:
            print(' '.join(reversed(arr)))
            return

        self.findPath(self.parent[s], arr)


print("노드, 간선 개수")
V, E = map(int, input().split())
g = Graph(V)
start = int(input("start vertex: "))
print("간선 정보를 입력하세요")
for _ in range(E):
    edge = [int(x) for x in input().split()]
    g.addEdge(edge[0], edge[1], edge[2])

g.dijkstra(start)

print("dist: {}".format(g.dist))
print("parent: {}".format(g.parent))

for i in range(V):
    print("{} -> {}의 경로".format(start, i))
    g.findPath(i, [])


