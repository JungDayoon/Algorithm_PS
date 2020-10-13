import sys

pos = [[1,0],[-1,0],[0,1],[0,-1]]

def isIn(y, x):
    if(y>=0 and y<N and x >=0 and x<M):
        return True
    return False

def bfs(y, x):
    cheeseDummy = {}
    queue = []
    queue.append((y, x))
    visited[y][x] = 0
    if y not in cheeseDummy.keys():
        cheeseDummy[y] = []
        cheeseDummy[y].append(x)

    while queue:
        curr = queue.pop(0)
        for i in range(4):
            ny = curr[0] + pos[i][0]
            nx = curr[1] + pos[i][1]

            if(isIn(ny, nx) and cheese[ny][nx] == 0 and visited[ny][nx] == 1):
                queue.append((ny, nx))
                visited[ny][nx] = 0
                # if ny not in cheeseDummy.keys():
                #     cheeseDummy[ny] = []
                # cheeseDummy[ny].append(nx)

    #모든 치즈 탐색 끝났으면
    # cheeseDummy_keys = list(cheeseDummy.keys())
    # for i in range(len(cheeseDummy_keys)):
    #     minNum = min(cheeseDummy[cheeseDummy_keys[i]])
    #     maxNum = max(cheeseDummy[cheeseDummy_keys[i]])
    #     for j in range(minNum, maxNum +1):
    #         cheeseTmp[cheeseDummy_keys[i]][j] = 1


N = 0 #세로
M = 0 #가로

N, M = map(int, input().split())
cheese = [[int(x) for x in input().split()]for y in range(N)]
time = 0
prev_cnt = 0

for i in range(N):
    prev_cnt += cheese[i].count(1)

while True:
    time +=1
    visited = [[1 for x in range(M)]for y in range(N)]
    # cheeseTmp = [[0 for x in range(M)]for y in range(N)]

    for i in range(N):
        if(cheese[i][0] == 0):
            bfs(i, 0)
        if(cheese[i][M-1] == 0):
            bfs(i, M-1)

    for i in range(M):
        if(cheese[0][i] == 0):
            bfs(0, i)
        if(cheese[N-1][i] == 0):
            bfs(N-1, i)

    # print(visited)

    erase = []
    for i in range(N):
        for j in range(M):
            if(cheese[i][j] == 1):
                for k in range(4):
                    ny = i + pos[k][0]
                    nx = j + pos[k][1]
                    if(visited[ny][nx] == 0):
                        erase.append((i, j))
                        break

    for i in range(len(erase)):
        cheese[erase[i][0]][erase[i][1]] = 0

    for i in range(N):
        for j in range(M):
            cheese[i][j] = visited[i][j] and cheese[i][j]

    # print(cheese)

    cnt = 0
    for i in range(N):
        cnt += cheese[i].count(1)
    # print(cnt)

    if cnt == 0:
        break
    
    prev_cnt = cnt

print(time)
print(prev_cnt)

    
    