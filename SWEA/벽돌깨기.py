import sys
import copy

pos = [[1,0],[-1,0],[0,1],[0,-1]]
N = 0
W = 0
H = 0
possible = []
answer = []

def isIn(x, y):
    if (x>=0 and x<W and y >=0 and y<H):
        return True
    return False

def crash(x, y, cnt, arr):
    arr[y][x] = 0
    for c in range(1, cnt):
        for i in range(0, 4):
            nx = x + pos[i][1]*c
            ny = y + pos[i][0]*c
            if(isIn(nx, ny) and arr[ny][nx] > 0):
                crash(nx, ny, arr[ny][nx], arr)

def removeEmpty(arr, possible):
    for i in range(0, W):
        tmp = [0 for x in range(H)]
        idx = H-1
        for j in range(H-1, -1, -1):
            if(arr[j][i] != 0):
                tmp[idx] = arr[j][i]
                arr[j][i]= 0
                idx -= 1
        for j in range(H):
            arr[j][i] = tmp[j]
        
        flag = 0
        for j in range(H):
            if(tmp[j] != 0):
                flag = 1
                possible[i] = j
                break
        if(flag == 0):
            possible[i] = H
        


def solution(now_c, goal_c, arr, possible):
    cnt = 0
    for i in range(H):
        cnt += arr[i].count(0)

    if(cnt == W*H):
        answer.append(0)
        return
    
    if(now_c == goal_c):
        cnt = 0
        for i in range(0, H):
            cnt += arr[i].count(0)
        answer.append(W*H - cnt)

        return
        
    for i in range(0, W):
        j = possible[i]
        if(j < H and arr[j][i] != 0):
            tmp_arr = copy.deepcopy(arr)
            tmp_possible = copy.deepcopy(possible)
            crash(i, j, arr[j][i], arr)
            removeEmpty(arr, possible)
            solution(now_c+1, goal_c, arr, possible)
            arr = copy.deepcopy(tmp_arr)
            possible = copy.deepcopy(tmp_possible)



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = []
    N, W, H = map(int, input().split())
    arr = [[int(x) for x in input().split()]for y in range(H)]
    possible = [0 for x in range(W)]

    for i in range(W):
        for j in range(H):
            if(arr[j][i] > 0): 
                possible[i] = j
                break
        
    solution(0, N, arr, possible)
    # print(str(min(answer)))
    print("#" + str(test_case) + " " + str(min(answer)))
    # "#" + test_case + " " + 
    # print(arr)
