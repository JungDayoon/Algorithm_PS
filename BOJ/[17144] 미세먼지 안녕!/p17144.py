def isIn(y, x):
    if 0 <= x < C and 0 <= y < R:
        return True
    return False


def copyMap(orig, new):
    for i in range(R):
        for j in range(C):
            new[i][j] = orig[i][j]


def dustSpread():
    global roomMap

    dustList = []
    for i in range(R):
        for j in range(C):
            if roomMap[i][j] > 0:  # 미세 먼지 있음
                dustList.append([i, j, roomMap[i][j]])
    roomMap = [[0 for _ in range(C)] for _ in range(R)]
    roomMap[cleaner[0][0]][cleaner[0][1]] = -1
    roomMap[cleaner[1][0]][cleaner[1][1]] = -1

    for dust in dustList:
        count = 0
        for i in range(1, 5):
            ny = dust[0] + pos[i][0]
            nx = dust[1] + pos[i][1]

            if isIn(ny, nx) and roomMap[ny][nx] != -1:
                roomMap[ny][nx] += dust[2] // 5
                count += 1
        dust[2] -= count * (dust[2] // 5)

    for dust in dustList:
        roomMap[dust[0]][dust[1]] += dust[2]


def circulate():
    newMap = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            dir = moveMap[i][j]
            newMap[i + pos[dir][0]][j + pos[dir][1]] = roomMap[i][j]
            if newMap[i + pos[dir][0]][j + pos[dir][1]] == -1:
                newMap[i + pos[dir][0]][j + pos[dir][1]] = 0

    newMap[cleaner[0][0]][cleaner[0][1]] = -1
    newMap[cleaner[1][0]][cleaner[1][1]] = -1

    copyMap(newMap, roomMap)

def getCount():
    cnt = 0
    for i in range(R):
        for j in range(C):
            if roomMap[i][j] > 0:
                cnt += roomMap[i][j]

    return cnt

R, C, T = map(int, input().split())
roomMap = [[int(x) for x in input().split()] for _ in range(R)]
moveMap = [[0 for _ in range(C)] for _ in range(R)]
pos = [[0, 0], [-1, 0], [0, -1], [1, 0], [0, 1]]

cleaner = []
for i in range(R):
    for j in range(C):
        if roomMap[i][j] == -1:
            cleaner.append([i, j])

for i in range(cleaner[0][0]+1):
    moveMap[i][0] = 3
    moveMap[i][C - 1] = 1

for i in range(cleaner[1][0], R):
    moveMap[i][0] = 1
    moveMap[i][C - 1] = 3

for j in range(1, C):
    moveMap[0][j] = 2
    moveMap[R - 1][j] = 2

for j in range(C-1):
    moveMap[cleaner[0][0]][j] = 4
    moveMap[cleaner[1][0]][j] = 4

for time in range(T):
    dustSpread()
    circulate()

print(getCount())