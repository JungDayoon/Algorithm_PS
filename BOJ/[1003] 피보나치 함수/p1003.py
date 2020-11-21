T = int(input())
t_c = []

for _ in range(T):
    t_c.append(int(input()))
dp = [[0, 0] for _ in range(max(t_c)+1)]

dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 0
dp[1][1] = 1

for i in range(2, max(t_c)+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for t in t_c:
    print(str(dp[t][0]) + " " + str(dp[t][1]))

