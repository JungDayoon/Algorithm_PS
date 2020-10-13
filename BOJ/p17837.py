N, K = map(int, input().split())
zoneInfo = [[2 for _ in range(N+2)] for _ in range(N+2)]
chessMap = [[[] for _ in range(N+2)] for _ in range(N+2)]
pos = [[0,1],[0,-1],[-1,0],[1,0]]
change = [1,-1,1,-1]
endFlag = False
endTurn = 0

def isEndCondition(y, x):
    if len(chessMap[y][x]) >= 4:
        return True
    return False

def updateMap(now_y, now_x, blue_flag, newList, target_dir):
    global endFlag

    new_y = now_y + pos[target_dir - 1][0]
    new_x = now_x + pos[target_dir - 1][1]

    if zoneInfo[new_y][new_x] == 0:  # white zone
        # update chessInfo, chessMap
        for nl in newList:
            chessInfo[nl[0]] = [new_y, new_x]
            chessMap[new_y][new_x].append(nl)
        if isEndCondition(new_y, new_x):
            endFlag = True
    elif zoneInfo[new_y][new_x] == 1:  # red zone
        newList.reverse()
        for nl in newList:
            chessInfo[nl[0]] = [new_y, new_x]
            chessMap[new_y][new_x].append(nl)
        if isEndCondition(new_y, new_x):
            endFlag = True
    elif zoneInfo[new_y][new_x] == 2:  # blue zone
        if blue_flag:
            for nl in newList:
                chessMap[now_y][now_x].append(nl)

        if not blue_flag:
            blue_flag = True
            target_dir += change[target_dir - 1]
            newList[0][1] = target_dir
            updateMap(now_y, now_x, blue_flag, newList, target_dir)

def moveChess():
    global endFlag
    for i in range(K): # 체스 번호 하나씩 옮김
        now_y = chessInfo[i][0]
        now_x = chessInfo[i][1]

        newList = []
        while True:
            chess = chessMap[now_y][now_x].pop()
            newList.insert(0, chess)
            if chess[0] == i:
                target_dir = chess[1]
                break

        updateMap(now_y, now_x, False, newList, target_dir)

        if endFlag:
            break

for i in range(1, N+1):
    Input = [int(x) for x in input().split()]
    for j in range(1, N+1):
        zoneInfo[i][j] = Input[j-1]

chessInfo = []
for i in range(K):
    chessInfo.append([int(x) for x in input().split()])

for i in range(K):
    y = chessInfo[i][0]
    x = chessInfo[i][1]
    Dir = chessInfo[i][2]

    chessMap[y][x].append([i, Dir])

for i in range(1001):
    moveChess()
    if endFlag:
        endTurn = i+1
        break

if not endFlag:
    endTurn = -1

print(endTurn)