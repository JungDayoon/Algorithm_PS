def fillMap(type, y, x, Map):
    if type == 3:
        for i in range(6):
            if Map[y][i] != 0 or Map[y+1][i] != 0:
                Map[y][i-1] = 1
                Map[y + 1][i-1] = 1
                break
        else:
            Map[y][i] = 1
            Map[y + 1][i] = 1

    else:
        for i in range(6):
            if Map[y][i] != 0:
                Map[y][i-1] = 1
                if type == 2:
                    Map[y][i-2] = 1
                break
        else:
            Map[y][i] = 1
            if type == 2:
                Map[y][i - 1] = 1



def checkEmptyLine(Map):
    global totalScore

    newMap = [[0 for _ in range(6)] for _ in range(4)]
    newIdx = 5
    for i in range(5, -1, -1):
        count = 0
        for j in range(4):
            if Map[j][i] == 1:
                count += 1
        if count == 4:
            totalScore += 1
        elif 0 < count < 4:
            for j in range(4):
                newMap[j][newIdx] = Map[j][i]
            newIdx -= 1

    for i in range(4):
        for j in range(6):
            Map[i][j] = newMap[i][j]


def checkSpecialLine(Map):
    newMap = [[0 for _ in range(6)] for _ in range(4)]

    removeLine = 0
    for i in range(2):
        count = 0
        for j in range(4):
            if Map[j][i] == 1:
                count += 1
        if count > 0:
            removeLine += 1

    MapIdx = 5 - removeLine
    for i in range(5, -1, -1):
        if MapIdx < 0:
            break
        for j in range(4):
            newMap[j][i] = Map[j][MapIdx]
        MapIdx -= 1

    for i in range(4):
        for j in range(6):
            Map[i][j] = newMap[i][j]


N = int(input())
blueMap = [[0 for _ in range(6)] for _ in range(4)]
greenMap = [[0 for _ in range(6)] for _ in range(4)]
changeType = [0, 1, 3, 2]
totalScore = 0

for _ in range(N):
    t, y, x = map(int, input().split())
    fillMap(t, y, x, blueMap)
    fillMap(changeType[t], x, y, greenMap)

    checkEmptyLine(blueMap)
    checkEmptyLine(greenMap)

    checkSpecialLine(blueMap)
    checkSpecialLine(greenMap)

blueScore = 0
greenScore = 0
for i in range(4):
    for j in range(6):
        blueScore += blueMap[i][j]
        greenScore += greenMap[i][j]

print(totalScore)
print(blueScore + greenScore)
