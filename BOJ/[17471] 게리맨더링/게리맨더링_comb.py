from itertools import combinations

def makePath(start, visited):
    visited[start] = True
    for Next in adj[start]:
        if not visited[Next]:
            makePath(Next, visited)

def possible(a, b):
    visited = [False for _ in range(N)]
    for s in a:
        visited[s] = True
    makePath(b[0], visited)
    if False not in visited:
        return True
    return False

def getSum(List):
    listSum = 0
    for l in List:
        listSum += people[l]

    return listSum


N = int(input())
people = [int(x) for x in input().split()]
peopleIdx = [int(x) for x in range(N)]
adj = [[] for _ in range(N)]
minList = []

for i in range(N):
    adj[i] = [int(x)-1 for x in input().split()]
    adj[i].pop(0)

for i in range(1, N//2+1):
    comb = list(combinations(peopleIdx, i))
    for c in comb:
        other = [int(x) for x in peopleIdx if x not in c]
        if possible(c, other) and possible(other, c):
            result = abs(getSum(c) - getSum(other))
            print("a: {}, b: {}, result: {}".format(c, other, result))
            minList.append(result)

print(-1 if len(minList) == 0 else min(minList))