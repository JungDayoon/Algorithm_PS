import copy
from itertools import combinations
from collections import deque
# def Combination(now_c, goal_c, prev, Virus):
#     if(now_c == goal_c):
#         activate_Virus.append(copy.deepcopy(Set))
#         return
    
#     for i in range(prev+1, len(Virus)):
#         Set.append(Virus[i])
#         Combination(now_c+1, goal_c, i, Virus)
#         Set.pop()

def isIn(y, x):
    if y >= 0 and x >= 0 and y <N and x <N:
        return True
    return False

def bfs(virus, Map):
    global v_c
    queue = deque()

    for v in virus:
        queue.append(v)
        Map[v[0]][v[1]] = 1
    
    maxValue = 1

    while queue:
        curr = queue.popleft()
        for i in range(4):
            ny = curr[0] + pos[i][0]
            nx = curr[1] + pos[i][1]

            if(isIn(ny, nx) and (Map[ny][nx] == 0 or Map[ny][nx] == -2)): # map에 포함되고 들리지 않은 곳이고 벽이 아니면
                queue.append([ny, nx])
                if Map[ny][nx] == 0:
                    v_c -= 1
                # virusMap[ny][nx] = 1
                Map[ny][nx] = Map[curr[0]][curr[1]]+1
                maxValue = Map[ny][nx]
                
                if v_c == 0:
                    return maxValue
        
    return -1

pos = [[1,0],[-1,0],[0,1],[0,-1]]

N, M = map(int, input().split())
Map = [[int(x) for x in input().split()]for y in range(N)]
# virusMap = [[0 for x in range(N)]for y in range(N)]

Virus = []
activate_Virus = []

flag = 0
answer = 1000000
virus_cnt = 0
required_cnt = 0

for i in range(N):
    for j in range(N):
        if(Map[i][j] == 0):
            flag = 1
            virus_cnt += 1
        if(Map[i][j] == 1):
            Map[i][j] = -1
        if(Map[i][j] == 2):
            Map[i][j] = -2
            Virus.append([i, j])

if flag == 0:
    print(0)

else:
    activate_Virus = list(combinations(Virus, M))

    # print(activate_Virus)

    tmp = []
    
    for i in range(len(activate_Virus)):
        tmpMap = [[] for _ in range(N)]
        for j in range(N):
            for k in range(N):
                tmpMap[j].append(Map[j][k])
        # tmpMap = copy.deepcopy(Map)
        v_c = virus_cnt
        maxValue = bfs(activate_Virus[i], tmpMap)
        if maxValue != -1:
            answer = min(answer, maxValue)
        tmp.append(maxValue)

    if(answer == 1000000):
        print(-1)
    else:
        print(answer-1)
