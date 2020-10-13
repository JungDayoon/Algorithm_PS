N, M = map(int, input().split())
tree = [int(x) for x in input().split()]

low = 0
high = 1000000000
answer = 0

while low <= high:
    mid = (low+high)//2
    count = 0
    for i in range(N):
        if(tree[i] > mid):
            count += tree[i]- mid
    
    if(count < M):
        high = mid -1
    else:
        answer = mid
        low = mid + 1

print(answer)
    
