N, M, K = map(int, input().split())
sharkMap = [[int(x) for x in input().split()] for _ in range(N)]
sharkDir = [int(x) - 1 for x in input().split()]
sharkPriority = [[[int(x) - 1 for x in input().split()] for _ in range(4)] for _ in range(M)]
sharkScent = [[[] for _ in range(N)] for _ in range(N)]
sharkInfo = []
pos = [[-1, 0], [1, 0], [0, -1], [0, 1]]    # 위, 아래, 왼쪽, 오른쪽 순으로 봄


def isIn(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def spreadScent(ny, nx, num):
    sharkScent[ny][nx] = [num, K]  # 향기 map에는 상어 번호와 향기 지속시간이 필요함


def timePass():
    for i in range(N):
        for j in range(N):
            if len(sharkScent[i][j]) > 0:
                sharkScent[i][j][1] -= 1
                if sharkScent[i][j][1] == 0:
                    sharkScent[i][j].clear()


def moveShark(y, x, num, Dir):
    global newShark
    sharkPos = sharkPriority[num][Dir]
    # 빈칸 우선순위 찾기
    for i in range(4):
        ny = y + pos[sharkPos[i]][0]
        nx = x + pos[sharkPos[i]][1]
        if isIn(ny, nx) and len(sharkScent[ny][nx]) == 0:
            newShark.append([ny, nx, num, sharkPos[i]])
            # spreadScent(y, x, num)
            return

    # 자기 냄새 우선순위 찾기
    for i in range(4):
        ny = y + pos[sharkPos[i]][0]
        nx = x + pos[sharkPos[i]][1]
        if isIn(ny, nx) and sharkScent[ny][nx][0] == num:
            newShark.append([ny, nx, num, sharkPos[i]])
            # spreadScent(y, x, num)
            return

def toMap(sharkInfo):
    arr = [[-1 for _ in range(N)] for _ in range(N)]
    for shark in sharkInfo:
        arr[shark[0]][shark[1]] = shark[2]
    return arr

for idx in range(M):
    for i in range(N):
        for j in range(N):
            if sharkMap[i][j] - 1 == idx:
                sharkInfo.append([i, j, idx, sharkDir[idx]])    # 상어 y, x, 번호, 방향
                spreadScent(i, j, idx)

# print(sharkInfo)
# print(sharkPriority)
time = 0
while time <= 1000:
    if len(sharkInfo) == 1:  # 1번 상어만 살아남음
        break

    # print("time: "+ str(time))
    # arr = toMap(sharkInfo)
    # for i in range(N):
    #     out = ""
    #     for j in range(N):
    #         out += str(arr[i][j]) + " "
    #     print(out)
    # print("\n")


    newShark = []
    while sharkInfo:
        shark = sharkInfo.pop()
        y = shark[0]
        x = shark[1]
        num = shark[2]
        Dir = shark[3]
        moveShark(y, x, num, Dir)
    # print(newShark)
    sharkInfo = newShark[:]
    sharkInfo = sorted(sharkInfo, key=lambda t: (t[0], t[1], t[2]))

    prev = sharkInfo[0]
    removeList = []
    for i in range(1, len(sharkInfo)):
        if prev[0] == sharkInfo[i][0] and prev[1] == sharkInfo[i][1]:  # 상어 같은 위치에 존재
            removeList.append(sharkInfo[i])
        prev = sharkInfo[i]

    for removeItem in removeList:
        rIdx = sharkInfo.index(removeItem)
        sharkInfo.pop(rIdx)

    timePass()

    for shark in sharkInfo:
        spreadScent(shark[0], shark[1], shark[2])

    time += 1
    # print(sharkInfo)

# print(time)
print(time if time <= 1000 else -1)
