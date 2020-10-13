def calculate(_num1, _num2, oper):
    num1 = int(_num1)
    num2 = int(_num2)

    if oper == '+':
        return num1+num2
    elif oper == '-':
        return num1-num2
    elif oper == '*':
        return num1*num2


def solution(prev, prev_num, operation):
    global maxSum

    for i in range(prev, len(Calcul)):
        tmp_num = prev_num
        tmp_oper = operation

        prev_num = calculate(prev_num, Calcul[i], operation)
        if i == len(Calcul)-2:
            operation = calculStr[i * 2 + 3]
            prev_num = calculate(prev_num, calculStr[N-1], operation)
            maxSum = max(maxSum, int(prev_num))
            prev_num = calculate(tmp_num, calculStr[i * 2], tmp_oper)
            operation = calculStr[i*2 + 1]
            continue
        if i == len(Calcul)-1:
            maxSum = max(maxSum, int(prev_num))
            prev_num = calculate(tmp_num, calculStr[i * 2], tmp_oper)
            operation = calculStr[i * 2 + 1]

            # 마지막 원소 하나 계산해주는 부분
            prev_num = calculate(prev_num, calculStr[N-1], operation)
            maxSum = max(maxSum, int(prev_num))
            continue
        operation = calculStr[i*2+3]
        solution(i+2, prev_num, operation)
        prev_num = calculate(tmp_num, calculStr[i * 2], tmp_oper)
        operation = calculStr[i * 2 + 1]




N = int(input())
calculStr = str(input())
# print(calculStr)

Calcul = []
prev = calculStr[0]

for i in range(0, N-2, 2):
    prev = calculate(prev, calculStr[i+2], calculStr[i+1])
    Calcul.append(calculate(calculStr[i], calculStr[i+2], calculStr[i+1]))


maxSum = prev
solution(0, "0", '+')
print(maxSum)