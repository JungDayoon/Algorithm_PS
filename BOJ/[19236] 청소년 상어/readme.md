# [BOJ 19236] 청소년 상어 - Python

### :computer: Algorithm

> 백트래킹, 시뮬레이션



### :computer: Logic

`fishMap`: 물고기(상어 포함)의 번호, 방향을 저장하는 2차원 리스트

1. 상어의 위치 초기화
2. 백트래킹 함수인 `moveShark(y, x, dir, eatNum)`를 호출한다.
   1. 물고기를 순서대로 이동시킨다.
   2. 상어를 움직일 수 있는 공간에 모두 움직여본다.
   3. `moveShark`를 호출한 후에는 다시 원래 `fishMap`으로 돌려놓는다.
   4. 상어를 움직일 수 없다면, 그 때 `maxEat`을 갱신한다.



### :computer: Review

> 걸린 시간: 1시간 30분

:bulb: **실수한 부분**

`moveOneFish(num)` 함수에서 옮기려는 자리가 비어있다면, 그 전자리를 0으로 만들어야 하는데 반대로 한 부분

`moveShark(y, x, dir, eatNum)` 함수에서 상어를 움직일 때, idx를 늘려가면서 하지 않은 부분. 이를 하지 않으면 계속 한 칸 옆만 볼 수 밖에 없다..

```python
ny = y + idx * pos[dir][0]
nx = x + idx * pos[dir][1]
```



자잘한 실수만 없었어도 더 빨리 풀 수 있었는데 아쉬움이 남는다 ㅠㅠ 

시험 때는 이러지말자 화이팅 !!!!!!!