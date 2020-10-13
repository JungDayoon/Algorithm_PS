N = int(input())
fishMap = [[int(x) for x in input().split()] for _ in range(N)]
pos = [[-1, 0],  [0, -1], [1, 0], [0, 1]]
sharkSize = 2
newShark = []
sharkList = []
flag = True
resTime = 0
fishCnt = 0


def isIn(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def moveShark(shark_y, shark_x):
    global flag, newShark, resTime, fishCnt

    time = 0
    queue = []
    queue.append([shark_y, shark_x])
    visited[shark_y][shark_x] = True

    while queue:
        queue = sorted(queue)

        for _ in range(len(queue)):
            curr = queue.pop(0)

            if 0 < fishMap[curr[0]][curr[1]] < sharkSize:
                # 잡아먹기
                fishMap[curr[0]][curr[1]] = 0
                newShark = [curr[0], curr[1]]
                resTime += time
                fishCnt += 1
                return

            for i in range(4):
                ny = curr[0] + pos[i][0]
                nx = curr[1] + pos[i][1]

                if isIn(ny, nx) and not visited[ny][nx] and fishMap[ny][nx] <= sharkSize:
                    # 지나갈 수 있음
                    visited[ny][nx] = True
                    queue.append([ny, nx])
        time += 1
    flag = False


for i in range(N):
    for j in range(N):
        if fishMap[i][j] == 9:  # 상어
            origShark = [i, j]

while True:
    if fishCnt == sharkSize:
        sharkSize += 1
        fishCnt = 0

    visited = [[False for _ in range(N)] for _ in range(N)]
    sharkList.append(origShark)
    moveShark(origShark[0], origShark[1])
    # 더이상 먹을 물고기가 없음
    if not flag:
        break
    # 상어 위치 변경
    fishMap[origShark[0]][origShark[1]] = 0
    fishMap[newShark[0]][newShark[1]] = 9
    origShark = newShark[:]

# print(sharkList)
print(resTime)
