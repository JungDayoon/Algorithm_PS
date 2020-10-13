import sys

def findOut():
    min_candidate = []
    sortedCandidate = sorted(candidate, key = lambda t: t[2])
    minCnt = min(candidate, key = lambda t: t[1])[1]

    for c in candidate:
        if(c[1] == minCnt):
            min_candidate.append(c)
    
    outItem = 0
    if(len(min_candidate) == 1):
        outItem = min_candidate
    else:
        outItem = sortedCandidate[len(sortedCandidate)-1]
    return outItem

def makeNewCandidate(pos, item):
    newCandidate = [item, 1, 1]
    for i in range(len(candidate)):
        candidate[i][2] += 1 #나갈 순서 하나 씩 올려주기
    
    candidate.insert(pos, newCandidate)

N = int(input())
M = int(input())

total = [int(x) for x in input().split()]
candidate = []

for i in range(M):
    candidate_idx = [c[0] for c in candidate]
    if(total[i] not in candidate_idx):
        if(len(candidate) < N): #사진틀 비어있음
            makeNewCandidate(len(candidate), total[i])
            # candidate.append(total[i])
        else:
            eraseItem = findOut()
            eraseIdx = candidate.index(eraseItem)
            candidate.remove(eraseItem)
            makeNewCandidate(eraseIdx, total[i])
    else:
        for j in range(len(candidate)):
            if(candidate[j][0] == total[i]):
                candidate[j][1] += 1

candidate = sorted(candidate, key = lambda t:t[0])
outStr = ""
for i in range(N):
    outStr += str(candidate[i][0]) + " "

print(outStr)        