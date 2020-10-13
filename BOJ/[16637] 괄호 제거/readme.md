# [BOJ 16637] 괄호 제거

### :computer: Algorithm

>  DFS, 브루트 포스



### :computer: Logic

`Calcul`: 괄호로 묶인 경우의 값들의 list 

ex) `3+8*7-9*2` 라면, [11, 56, -2, 18] 이 된다.

`calculate(_num1, _num2, oper)`: 두 숫자를 연산자 oper(+, -, *)로 계산한다.

`solution(prev, prev_num, operation)`

`prev`: 연산식 중 현재 보기 시작할 부분

`prev_num`: 그 전까지 연산완료한 수

`operation`: prev_num과 현재 볼 수와 연산할 연산자(+, -, * 중 하나)

- **괄호를 만든 경우**

  ```python
  prev_num = calculate(prev_num, Calcul[i], operation)
  operation = calculStr[i*2+3]
  solution(i+2, prev_num, operation)
  ```

  -> **이 때 확인해야 될 부분**

  -  `Calcul의 길이 - 2`까지 본 경우, 즉 위의 예시에서 ~*(7-9)까지 만든 경우라면 그 뒤에 하나 남은 원소는 괄호를 만들 수 없고 그냥 계산해야하므로 이를 처리해야한다.

  ```python
  if i == len(Calcul)-2:
      operation = calculStr[i * 2 + 3]
      prev_num = calculate(prev_num, calculStr[N-1], operation)
      maxSum = max(maxSum, int(prev_num))
      prev_num = calculate(tmp_num, calculStr[i * 2], tmp_oper)
      operation = calculStr[i*2 + 1]
      continue
  ```

  - `Calcul의 길이 - 1`까지 본 경우, 즉 위의 예시에서 ~-(9*2)까지 만든 경우라면 이 때의 sum과 maxSum을 비교하여 갱신하고, 괄호 없이 풀어 쓴 경우도 계산해준다.

  

- **괄호를 만들지 않은 경우**

  ```python
  prev_num = calculate(tmp_num, calculStr[i * 2], tmp_oper)
  operation = calculStr[i * 2 + 1]
  ```

  

### :computer: Review

> 걸린 시간: 1시간 40분

너무 어렵게 푼 것 같당 ,, 다른 사람들 코드보니까 훨씬 더 간단하게 풀었던데 괄호 제거2도 있다니까 다음에 풀 때는 좀 더 간단하고 직관적으로 짜야겠다.

