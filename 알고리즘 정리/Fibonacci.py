import time

# TOP-DOWN 방식
def fibonacci_TD(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fibonacci_TD(n-1) + fibonacci_TD(n-2)


# BOTTOM-UP 방식
def fibonacci_BU(n):
    global fibArr

    for i in range(3, n+1):
        fibArr[i] = fibArr[i-1] + fibArr[i-2]

    return fibArr[n]


# Loop 방식
def fibonacci_Loop(n):
    a = 1
    b = 2
    sum = 0
    for i in range(3, n+1):
        sum = a + b
        a = b
        b = sum

    return sum


N = int(input())
fibArr = [0 for _ in range(N+1)]
fibArr[1] = 1
fibArr[2] = 2

start = time.time()
result_TD = fibonacci_TD(N)
print("TOP-DOWN: {}, takes {}".format(result_TD, time.time() - start))

start = time.time()
result_BU = fibonacci_BU(N)
print("BOTTOM-UP: {}, takes {}".format(result_BU, time.time() - start))

start = time.time()
result_Loop = fibonacci_Loop(N)
print("LOOP: {}, takes {}".format(result_Loop, time.time() - start))

