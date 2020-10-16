def copyMap(orig, new):
    for i in range(N):
        for j in range(M):
            new[i][j] = orig[i][j]


def moveMarble(now, goal):
    global flag
    global redinHole, blueinHole
    global marbleList

    if flag:
        return

    if now == goal:
        if redinHole and not blueinHole:  # 되는 경우
            flag = True
        return

    tmpList = marbleList[:]
    tmpMap = [[0 for _ in range(M)] for _ in range(N)]
    copyMap(Map, tmpMap)

    for i in range(4):
        nowDir = i

        if nowDir == 0:
            marbleList = sorted(marbleList, key=lambda t: t[0])
        elif nowDir == 1:
            marbleList = sorted(marbleList, key=lambda t: t[0], reverse=True)
        elif nowDir == 2:
            marbleList = sorted(marbleList, key=lambda t: t[1])
        elif nowDir == 3:
            marbleList = sorted(marbleList, key=lambda t: t[1], reverse=True)

        enterFlag = False
        for m in range(len(marbleList)):
            holeFlag = False
            marble = marbleList[m]
            cy = marble[0]
            cx = marble[1]
            Map[cy][cx] = 0
            ny = cy + pos[nowDir][0]
            nx = cx + pos[nowDir][1]
            while Map[ny][nx] == 0 or Map[ny][nx] == 1:
                enterFlag = True
                if Map[ny][nx] == 1:
                    holeFlag = True
                    if marble[2] == 2:  # red
                        redinHole = True
                    elif marble[2] == 3:  # blue
                        blueinHole = True
                    break
                cy = ny
                cx = nx
                ny = cy + pos[nowDir][0]
                nx = cx + pos[nowDir][1]
            marbleList[m] = [cy, cx, marble[2]]
            if not holeFlag:
                Map[cy][cx] = marble[2]

        if enterFlag and not blueinHole:
            moveMarble(now + 1, goal)
        if flag:
            return
        marbleList = tmpList[:]
        redinHole = False
        blueinHole = False
        copyMap(tmpMap, Map)


N, M = map(int, input().split())
Map = [[0 for _ in range(M)] for _ in range(N)]
marbleList = []
pos = [[-1, 0], [1, 0], [0, -1], [0, 1]]
redinHole = False
blueinHole = False
flag = False

for i in range(N):
    Str = str(input())
    for j in range(M):
        if Str[j] == "#":
            Map[i][j] = -1
        elif Str[j] == ".":
            Map[i][j] = 0
        elif Str[j] == "O":
            Map[i][j] = 1
        elif Str[j] == "R":
            Map[i][j] = 2
            marbleList.append([i, j, 2])
        elif Str[j] == "B":
            Map[i][j] = 3
            marbleList.append([i, j, 3])

time = 0
while True:
    time += 1
    if time > 10:
        break
    moveMarble(0, time)
    if flag:
        break

print(time if time <= 10 else -1)
