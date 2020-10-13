S = int(input())

low = 0
high = S
answer = 0

while low <= high:
    mid = (low+high)//2
    Sum = mid * (mid+1) //2 
    
    if(Sum > S):
        high = mid -1
    else:
        answer = mid
        low = mid + 1

print(answer)