def moveFireBall():
    fireballMap = [[[] for _ in range(N)]for _ in range(N)]
    while fireballList:
        fireball = fireballList.pop()
        ny = (fireball._y + pos[fireball._d][0] * fireball._s % N)%N
        nx = (fireball._x + pos[fireball._d][1] * fireball._s % N)%N

        fireballMap[ny][nx].append([fireball._m, fireball._s, fireball._d])
    
    for i in range(N):
        for j in range(N):
            if len(fireballMap[i][j]) == 1:
                fireballList.append(FireBall(i, j, fireballMap[i][j][0][0], fireballMap[i][j][0][1], fireballMap[i][j][0][2]))
            
            elif len(fireballMap[i][j]) > 1:
                s_Sum = 0
                m_Sum = 0
                evenFlag = False
                oddFlag = False
                for fb in fireballMap[i][j]:
                    m_Sum += fb[0]
                    s_Sum += fb[1]
                    if fb[2] % 2 == 0:
                        evenFlag = True
                    else:
                        oddFlag = True
                
                newM = m_Sum // 5
                if newM == 0:
                    continue
                newS = s_Sum // len(fireballMap[i][j])
                if evenFlag and oddFlag:
                    for newD in range(1, 8, 2):
                        fireballList.append(FireBall(i, j, newM, newS, newD))
                else:
                    for newD in range(0, 7, 2):
                        fireballList.append(FireBall(i, j, newM, newS, newD))


N, M, K = map(int, input().split())
fireballList = []
pos = [[-1, 0], [-1, 1], [0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

class FireBall:
    def __init__(self, y, x, m, s, d):
        self._y = y
        self._x = x
        self._m = m
        self._s = s
        self._d = d
    
    def getCount(self):
        return self._m

for _ in range(M):
    y, x, m, s, d = map(int, input().split())
    fireballList.append(FireBall(y-1, x-1, m, s, d))

for k in range(K):
    moveFireBall()

count = 0
for f in fireballList:
    count += f.getCount()

print(count)