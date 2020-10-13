import sys

T = int(input())
N = 0
M = 0

def isFirst(paper):
    start = paper[0][1]
    # print(start)
    for i in range(1, len(paper)):
        if(start < paper[i][1]):
            return False
    return True


for test_case in range(T):
    N, M = map(int, input().split())
    tmp = [int(x) for x in input().split()]
    paper = []
    for i in range(N):
        paper.append((i, tmp[i]))
    
    # sortedPaper = sorted(paper, key = lambda x : -x[1])
    # print(sortedPaper)

    cnt = 0
    answer = 0
    while True:
        if(isFirst(paper)):
            cnt += 1
            if(paper.pop(0)[0] == M):
                break
        else:
            paper.append(paper.pop(0))
    
    print(cnt)

    