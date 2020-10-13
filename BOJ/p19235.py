def moveBlock(map, type, standard):
    flag = False
    if type == 1:  # 1x1
        for i in range(6):
            if map[standard][i] != 0:
                flag = True
                break
        if not flag:
            map[standard][i] = type
        else:
            map[standard][i - 1] = type

    elif type == 2:  # 1x2
        for i in range(6):
            if map[standard][i] != 0:
                flag = True
                break
        if not flag:
            map[standard][i - 1] = type
            map[standard][i] = type
        else:
            map[standard][i - 2] = type
            map[standard][i - 1] = type

    elif type == 3:  # 2x1
        for i in range(6):
            for j in range(standard, standard + 2):
                if map[j][i] != 0:
                    flag = True
                    break
            if flag:
                break
        if not flag:
            map[standard][i] = type
            map[standard + 1][i] = type
        else:
            map[standard][i - 1] = type
            map[standard + 1][i - 1] = type


def removeEmptySpace(map, maxRow):
    for i in range(maxRow, -1, -1):
        for j in range(3, -1, -1):
            if map[j][i] == 2 or map[j][i] == 1:
                new = i + 1
                while new < 6 and map[j][new] == 0:
                    map[j][new] = map[j][new - 1]
                    map[j][new - 1] = 0
                    new = new + 1
            elif j < 3 and map[j][i] == 3 and map[j + 1][i] == 3:
                new = i + 1
                while new < 6 and map[j][new] == 0 and map[j + 1][new] == 0:
                    map[j][new] = 3
                    map[j + 1][new] = 3
                    map[j][new - 1] = 0
                    map[j + 1][new - 1] = 0
                    new = new + 1

def removeLine(map):
    global score

    while True:
        flag = False
        maxRow = 0
        for i in range(6):
            count = 0
            for j in range(4):
                if map[j][i] > 0:
                    count += 1
            if count == 4:  # 지우기
                maxRow = max(maxRow, i)
                score += 1
                flag = True
                for j in range(4):
                    map[j][i] = 0
        if not flag:
            break
        removeEmptySpace(map, maxRow)


def specialLine(map):
    line0Cnt = 0
    line1Cnt = 0

    for j in range(4):
        if map[j][0] != 0:
            line0Cnt += 1

    for j in range(4):
        if map[j][1] != 0:
            line1Cnt += 1

    if line1Cnt > 0 and line0Cnt > 0:  # 오른쪽 두칸 비우기
        for i in range(4):
            map[i][5] = 0
            map[i][4] = 0
        removeEmptySpace(map, 3)

    elif line1Cnt > 0 and line0Cnt == 0:  # 오른쪽 한칸 비우기
        for i in range(4):
            map[i][5] = 0
        removeEmptySpace(map, 4)



N = int(input())
blue = [[0 for _ in range(6)] for _ in range(4)]
green = [[0 for _ in range(6)] for _ in range(4)]
changeType = [0, 1, 3, 2]
score = 0
blue_cnt = 0
green_cnt = 0
# i = x, j = y
for n in range(N):
    type, x, y = map(int, input().split())

    moveBlock(blue, type, x)
    moveBlock(green, changeType[type], y)

    removeLine(blue)
    removeLine(green)

    specialLine(blue)
    specialLine(green)

    removeLine(blue)
    removeLine(green)

for i in range(4):
    blue_cnt += blue[i].count(0)
    green_cnt += green[i].count(0)

print("{}\n{}".format(score, 4 * 6 - blue_cnt + 4 * 6 - green_cnt))