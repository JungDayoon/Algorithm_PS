from collections import deque

N = int(input())
K = int(input())
appleLoc = [[int(x) for x in input().split()] for _ in range(K)]
L = int(input())
changeInfo = [[x for x in input().split()] for _ in range(L)]
Map = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
pos = [[0, 1], [-1, 0], [0, -1], [1, 0]]

for i in range(N + 2):
    Map[i][0] = -1
    Map[i][N + 1] = -1
    Map[0][i] = -1
    Map[N + 1][i] = -1

for al in appleLoc:
    Map[al[0]][al[1]] = 1

time = 0
process = 0
dir = 0
snake = deque()
snake.append([1, 1])

while True:
    head = snake[len(snake) - 1]
    newHead_y = head[0] + pos[dir][0]
    newHead_x = head[1] + pos[dir][1]

    if Map[newHead_y][newHead_x] == -1:  # 게임종료
        break
    if Map[newHead_y][newHead_x] == 0:
        tail = snake.popleft()
        Map[tail[0]][tail[1]] = 0

    snake.append([newHead_y, newHead_x])
    Map[newHead_y][newHead_x] = -1

    time += 1
    if process < len(changeInfo):
        if time == int(changeInfo[process][0]):
            if changeInfo[process][1] == 'L':
                dir = (dir + 1) % 4
            else:
                dir = (dir + 3) % 4
            # dir += dirInfo[changeInfo[process][1]]
            process += 1

print(time + 1)
