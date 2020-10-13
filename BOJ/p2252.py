from collections import deque

N, M = map(int, input().split())
degree = [0 for x in range(N)]
# visited = [False for x in range(N)]
adjacency = [[] for x in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    adjacency[A].append(B)
    degree[B] += 1

queue = deque()

for i in range(N):
    if(degree[i] == 0):
        queue.append(i)

outStr = ""
while queue:
    curr = queue.popleft()
    outStr += str(curr+1) + " "
    for i in range(len(adjacency[curr])):
        degree[adjacency[curr][i]] -= 1
        if(degree[adjacency[curr][i]] == 0):
            queue.append(adjacency[curr][i])

print(outStr)