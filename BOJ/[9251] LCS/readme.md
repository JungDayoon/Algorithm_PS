# [BOJ 9251] LCS - Java

### :computer: Algorithm

> 다이나믹 프로그래밍



### :computer: Logic

:bulb: **점화식**

LCS(Xi, Yj) = LCS(Xi-1, Yj-1) + 1 								 (if str1[i] == str2[j])

​					 max(LCS(Xi-1, Yj), LCS(Xi, Yj-1))			(if str1[i] != str2[j])



### :computer: Review

백트래킹으로 풀면 시간초과가 난다 !!