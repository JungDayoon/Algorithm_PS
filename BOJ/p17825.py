

def playGame(Permutation):
    global Map
    global player
    global resultSum

    count = 0
    print(Permutation)
    for i in range(len(Permutation)):
        move = dice[i]

        p = player[Permutation[i]]
        # print(p)
        playerLoc = p[0]
        playerState = p[1]
        if playerLoc == 45: #이미 끝까지 움직임
            continue
        for _ in range(move):
            playerLoc = Map[playerState][playerLoc]
            if playerLoc == 25:  # state green으로
                playerState = green
            if playerLoc == 40:
                playerState = green
            if playerLoc == 45:  # 종료조건
                break

        prev_State = p[1]
        prev_Loc = p[0]

        p[0] = playerLoc
        p[1] = playerState

        if p[0] == 10 or p[0] == 20 or p[0] == 30:
            p[1] = blue
        if p[0] == 25:  # state green으로
            p[1] = green
        if p[0] == 40:
            p[1] = green

        if playerLoc != 45 and visited[p[1]][p[0]]:  # 불가능한 경우
            return
        if playerLoc == 45:
            continue

        count += p[0]
        visited[p[1]][p[0]] = True
        visited[prev_State][prev_Loc] = False


    resultSum = max(count, resultSum)

def makePermutation(now, goal):
    global pieces
    global Permutation
    if now == goal:
        Permutation.append(pieces[:])
        return
    for i in range(4):
        pieces[now] = i
        makePermutation(now + 1, goal)


dice = [int(x) for x in input().split()]
Map = [{}, {10: 13, 13: 16, 16: 19, 19: 25, 20: 22, 22: 24,
            24: 25, 30: 28, 28: 27, 27: 26, 26: 25}, {}]
red = 0
blue = 1
green = 2
resultSum = 0


for i in range(0, 39, 2):
    Map[red][i] = i + 2

for i in range(25, 41, 5):
    Map[green][i] = i + 5

# print(Map)
Permutation = []
pieces = [0 for _ in range(10)]
makePermutation(0, 10)
# if len(Permutation) == 4 ** 10:
#     print("True")
# print(Permutation)

for item in Permutation:
    # print(item)
    player = [[0, red], [0, red], [0, red], [0, red]]
    visited = [[False for _ in range(46)] for _ in range(3)]
    playGame(item)
print(resultSum)
