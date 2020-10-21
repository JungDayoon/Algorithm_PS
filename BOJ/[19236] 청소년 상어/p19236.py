def isIn(y, x):
    if 0 <= x < 4 and 0 <= y < 4:
        return True
    return False


def copyMap(orig, new):
    for i in range(4):
        for j in range(4):
            new[i][j] = orig[i][j][:]


def moveOneFish(num):
    for i in range(4):
        for j in range(4):
            if fishMap[i][j][0] == num:
                dir = fishMap[i][j][1]
                for r in range(8):
                    ny = i + pos[dir][0]
                    nx = j + pos[dir][1]
                    if isIn(ny, nx) and fishMap[ny][nx][0] != -1:  # 이동 가능
                        fishMap[i][j][1] = dir
                        fishMap[i][j], fishMap[ny][nx] = fishMap[ny][nx], fishMap[i][j]

                        # newNum = fishMap[ny][nx][0]
                        # newDir = fishMap[ny][nx][1]
                        # fishMap[ny][nx][0] = num
                        # fishMap[ny][nx][1] = dir
                        #
                        # if newNum == 0:
                        #     fishMap[i][j][0] = newNum
                        #     fishMap[i][j][1] = newDir
                        # else:
                        # fishMap[i][j] = [newNum, newDir]
                        return
                    else:
                        dir = (dir + 1)
                        if dir == 9:
                            dir = 1


def moveFish():
    for num in range(1, 17):
        moveOneFish(num)


def moveShark(y, x, dir, eatNum):
    global maxEat

    moveFish()

    tmpMap = [[[0, 0] for _ in range(4)] for _ in range(4)]
    copyMap(fishMap, tmpMap)

    isAct = False
    idx = 1
    while True:
        ny = y + idx * pos[dir][0]
        nx = x + idx * pos[dir][1]

        if not isIn(ny, nx):
            break

        if fishMap[ny][nx][0] != 0:  # 상어 움직일 수 있음
            isAct = True
            food = fishMap[ny][nx][0]
            fishMap[ny][nx][0] = -1
            fishMap[y][x][0] = 0
            fishMap[y][x][1] = 0

            moveShark(ny, nx, fishMap[ny][nx][1], eatNum + food)
            copyMap(tmpMap, fishMap)
        idx += 1

    if not isAct:
        maxEat = max(maxEat, eatNum)


pos = [[], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
fishMap = [[[0, 0] for _ in range(4)] for _ in range(4)]
# fishList = [[0,0,0]]
eatNum = 0
maxEat = 0

for i in range(4):
    tmp = [int(x) for x in input().split()]
    for j in range(8):
        fishMap[i][j // 2][j % 2] = tmp[j]

# 상어 초기화
# 상어 번호 : -1
eatNum += fishMap[0][0][0]
fishMap[0][0][0] = -1
shark_y = 0
shark_x = 0
shark_dir = fishMap[0][0][1]

moveShark(shark_y, shark_x, shark_dir, eatNum)

print(maxEat)
