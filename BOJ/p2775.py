import sys

T = int(input())
apartment = [[0 for x in range(15)]for y in range(15)]

for i in range(15):
    apartment[0][i] = i

last = 1

for t in range(T):
    k = int(input()) #층
    n = int(input()) #호

    for i in range(1, k+1):
        for j in range(1, n+1):
            apartment[i][j] = apartment[i][j-1] + apartment[i-1][j]

    print(apartment[k][n])
