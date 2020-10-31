def makePath(start, visited):
    visited[start] = True
    for Next in adj[start]:
        if not visited[Next]:
            visited[Next] = True
            makePath(Next, visited)


def getMin(num, Set):
    if len(Set) == N:
        return
    other = [int(x) for x in peopleIdx if x not in Set]
    visited = [False for _ in range(N)]
    for s in Set:
        visited[s] = True
    makePath(other[0], visited)
    if False not in visited:
        result = abs(getSum(Set) - getSum(other))
        print("a: {}, b: {}, result: {}".format(Set, other, result))
        minList.append(result)

    visited = [False for _ in range(N)]
    for s in Set:
        visited[s] = True
    for Next in adj[num]:
        if visited[Next]:
            continue
        visited[Next] = True
        Set.append(Next)
        getMin(Next, Set)
        visited[Next] = False
        Set.pop()


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

for i in range(N):
    peopleSet = [i]
    getMin(i, peopleSet)

print(-1 if len(minList) == 0 else min(minList))