def isIn(y, x):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


N, M, K = map(int, input().split())
treeMap = [[[] for _ in range(N)] for _ in range(N)]
food = [[5 for _ in range(N)] for _ in range(N)]
addFood = [[int(x) for x in input().split()] for _ in range(N)]
pos = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for _ in range(M):
    y, x, z = map(int, input().split())
    y -= 1
    x -= 1
    treeMap[y][x].append(z)

for year in range(K):
    treeList = []
    for i in range(N):
        for j in range(N):
            if len(treeMap[i][j]) > 0:
                deadTree = []

                treeMap[i][j] = sorted(treeMap[i][j])
                for idx in range(len(treeMap[i][j])):
                    tree = treeMap[i][j][idx]
                    if food[i][j] >= tree:
                        food[i][j] -= tree
                        treeMap[i][j][idx] += 1  # 나이 먹음
                        treeList.append([i, j, treeMap[i][j][idx]])
                    else:
                        deadTree = treeMap[i][j][idx:]
                        treeMap[i][j] = treeMap[i][j][:idx]
                        break
                for dTree in deadTree:
                    food[i][j] += dTree // 2

    for tree in treeList:
        if tree[2] % 5 == 0:
            for p in range(8):
                ny = tree[0] + pos[p][0]
                nx = tree[1] + pos[p][1]

                if isIn(ny, nx):
                    treeMap[ny][nx].append(1)

    for i in range(N):
        for j in range(N):
            food[i][j] += addFood[i][j]

resTree = 0
for i in range(N):
    for j in range(N):
        resTree += len(treeMap[i][j])

print(resTree)
