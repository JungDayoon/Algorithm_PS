def moveDice(inst):
    newDice = [0 for _ in range(7)]
    for i in range(7):
        newDice[i] = dice[dir[inst][i]]

    return newDice[:]

def isIn(y, x):
    if 0 <= x < M and 0 <= y < N:
        return True
    return False

N, M, y, x, K = map(int, input().split())
Map = [[int(x) for x in input().split()] for _ in range(N)]
pos = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
instructionList = [int(x) for x in input().split()]
dice = [0 for _ in range(7)]
dir = [[], [0, 4, 2, 1, 6, 5, 3], [0, 3, 2, 6, 1, 5, 4], [0, 5, 1, 3, 4, 6, 2], [0, 2, 6, 3, 4, 1, 5]]

for instruction in instructionList:
    ny = y + pos[instruction][0]
    nx = x + pos[instruction][1]

    if not isIn(ny, nx):
        continue
    y = ny
    x = nx

    dice = moveDice(instruction)
    if Map[y][x] == 0:
        Map[y][x] = dice[6]
    else:
        dice[6] = Map[y][x]
        Map[y][x] = 0
    print(dice[1])
