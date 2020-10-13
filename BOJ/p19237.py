N, M, K = map(int, input().split())
sharkMap = [[int(x) for x in input().split()] for _ in range(N)]
sharkDir = [int(x) - 1 for x in input().split()]
sharkPriority = [[[int(x) - 1 for x in input().split()] for _ in range(4)] for _ in range(M)]
sharkScent = [[[-1, 0] for _ in range(N)] for _ in range(N)]     # num, time
sharkInfo = []
pos = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 위, 아래, 왼쪽, 오른쪽 순으로 봄


def isIn(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def spreadScent(ny, nx, num):
    sharkScent[ny][nx][0] = num
    sharkScent[ny][nx][1] = K



def timePass():
    for i in range(N):
        for j in range(N):
            if sharkScent[i][j][1] > 0:
                sharkScent[i][j][1] -= 1
                if sharkScent[i][j][1] == 0:
                    sharkScent[i][j][0] = -1


def moveShark(idx):
    global sharkInfo
    global removeList
    global arr
    Shark = sharkInfo[idx]
    sharkPos = sharkPriority[Shark[2]][Shark[3]]
    prev_y = Shark[0]
    prev_x = Shark[1]
    # 빈칸 우선순위 찾기
    for i in range(4):
        ny = Shark[0] + pos[sharkPos[i]][0]
        nx = Shark[1] + pos[sharkPos[i]][1]
        if isIn(ny, nx) and arr[ny][nx] != -1:
            removeList.append([ny, nx, Shark[2]])
        elif isIn(ny, nx) and sharkScent[ny][nx][1] == 0:
            sharkInfo[idx] = [ny, nx, Shark[2], sharkPos[i]]
            spreadScent(prev_y, prev_x, Shark[2])
            return

    # 자기 냄새 우선순위 찾기
    for i in range(4):
        ny = Shark[0] + pos[sharkPos[i]][0]
        nx = Shark[1] + pos[sharkPos[i]][1]
        if isIn(ny, nx) and sharkScent[ny][nx][0] == Shark[2]:
            sharkInfo[idx] = [ny, nx, Shark[2], sharkPos[i]]
            spreadScent(prev_y, prev_x, Shark[2])
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
                sharkInfo.append([i, j, idx, sharkDir[idx]])  # 상어 y, x, 번호, 방향

# print(sharkInfo)
# print(sharkPriority)
flag = False
removeList = []
for time in range(1001):
    print("turn " + str(time))
    arr = toMap(sharkInfo)

    for i in range(N):
        out = ""
        for j in range(N):
            out += str(arr[i][j]) + " "
        print(out)
    print("\n")

    if len(sharkInfo) == 1:  # 1번 상어만 살아남음
        flag = True
        print(time)
        break
    # newShark = []
    sharkInfo = sorted(sharkInfo, key=lambda t: (t[2]))     # 상어 num 기준으로 sort
    for idx in range(len(sharkInfo)):
        moveShark(idx)
    # print(newShark)
    # sharkInfo = newShark[:]


    # prev = sharkInfo[0]
    removeList = []
    # for i in range(1, len(sharkInfo)):
    #     if prev[0] == sharkInfo[i][0] and prev[1] == sharkInfo[i][1]:  # 상어 같은 위치에 존재
    #         removeList.append(sharkInfo[i])
    #     prev = sharkInfo[i]

    for removeItem in removeList:
        rIdx = sharkInfo.index(removeItem)
        sharkInfo.pop(rIdx)

    timePass()


# print(time)
if not flag:
    print(-1)
