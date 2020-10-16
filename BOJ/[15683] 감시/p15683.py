def isIn(y, x):
    if 0 <= x < M and 0 <= y < N:
        return True
    return False


def markMap(y, x, dir):
    ny = y + pos[dir][0]
    nx = x + pos[dir][1]
    while isIn(ny, nx) and Map[ny][nx] != 6:
        Map[ny][nx] = 1
        ny += pos[dir][0]
        nx += pos[dir][1]


def copyMap(orig, new):
    for i in range(N):
        for j in range(M):
            new[i][j] = orig[i][j]


def getCount():
    count = 0
    for i in range(N):
        for j in range(M):
            if Map[i][j] > 0:
                count += 1
    return count


def getArea(now, goal):
    global maxCount

    if now == goal:
        maxCount = max(maxCount, getCount())
        return

    tmpMap = [[0 for _ in range(M)] for _ in range(N)]
    copyMap(Map, tmpMap)
    for dir in CCTV[cctvList[now][2]]:
        for i in dir:
            markMap(cctvList[now][0], cctvList[now][1], i)
        getArea(now + 1, goal)
        copyMap(tmpMap, Map)


N, M = map(int, input().split())
Map = [[int(x) for x in input().split()] for _ in range(N)]
pos = [[-1, 0], [1, 0], [0, -1], [0, 1]]
CCTV = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [0, 3], [1, 2], [1, 3]],
        [[0, 2, 3], [0, 1, 2], [0, 1, 3], [1, 2, 3]], [[0, 1, 2, 3]]]
maxCount = 0
cctvList = []

for i in range(N):
    for j in range(M):
        if 0 < Map[i][j] < 6:
            cctvList.append([i, j, Map[i][j]])

getArea(0, len(cctvList))
print(N * M - maxCount)
