def checkHorizontal(num):
    global erase_set
    for j in range(M-1):
        if circle[num][j] == 0:
            continue
        if circle[num][j] == circle[num][j+1]:
            erase_set.add((num, j))
            erase_set.add((num, j+1))
    if circle[num][M-1] != 0 and circle[num][M-1] == circle[num][0]:
        erase_set.add((num, M-1))
        erase_set.add((num, 0))

def checkVertical(num):
    global erase_set
    for j in range(1, N):
        if circle[j][num] == 0:
            continue
        if circle[j][num] == circle[j+1][num]:
            erase_set.add((j, num))
            erase_set.add((j+1, num))

def rotate(num, dir, k):
    k %= len(circle[num])
    if dir == 0: #시계방향
        left = circle[num][:-k]
        right = circle[num][-k:]
        return right + left
    else: #반시계방향
        left = circle[num][:k]
        right = circle[num][k:]
        return right + left

def processAverage():
    Sum = 0
    Cnt = 0
    for i in range(1, N+1):
        for j in range(M):
            if(circle[i][j] == 0):
                continue
            Sum += circle[i][j]
            Cnt += 1
    
    Average = Sum / Cnt
    for i in range(1, N+1):
        for j in range(M):
            if(circle[i][j] == 0):
                continue
            if(circle[i][j] > Average):
                circle[i][j] -= 1
            elif(circle[i][j] < Average):
                circle[i][j] += 1

N, M, T = map(int, input().split())
circle = [[] for y in range(N+1)]

for i in range(1, N+1):
    circle[i] = [int(x) for x in input().split()]


circle_sum = 0
cnt = 0

while cnt < T:
    x, d, k = map(int, input().split())
    tmp = x
    while x <= N:
        circle[x] = rotate(x, d, k)
        x += tmp
    
    erase_set = set()

    for i in range(1, N+1):
        checkHorizontal(i)
    
    for i in range(M):
        checkVertical(i)
    
    erase_list = list(erase_set)
    if(len(erase_list) == 0):
        processAverage()
    else:
        for item in erase_list:
            circle[item[0]][item[1]] = 0
    
    circle_sum = 0
    for i in range(1, N+1):
        for j in range(M):
            circle_sum += circle[i][j]

    if circle_sum == 0:
        break
    cnt += 1
    
print(int(circle_sum))