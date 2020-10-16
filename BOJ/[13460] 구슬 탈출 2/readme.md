# [BOJ 13460] 구슬 탈출 2

### :computer: Algorithm

> 브루트포스, 시뮬레이션



### :computer: Logic

`Map`: 구슬, 빈칸, 구멍의 위치를 나타내는 2차원 리스트

`marbleList`: 빨간색 구슬과 파란색 구슬의 좌표를 담은 리스트

횟수를 늘려가면서 `moveMarble` 함수를 호출한다.

네 방향으로 구슬을 굴릴 수 있는 데, 각각의 방향에 따라 어느 구슬을 먼저 굴려야할 지가 다르므로 이를 구현해준다.

```python
if nowDir == 0:
	marbleList = sorted(marbleList, key=lambda t: t[0])
elif nowDir == 1:
	marbleList = sorted(marbleList, key=lambda t: t[0], reverse=True)
elif nowDir == 2:
	marbleList = sorted(marbleList, key=lambda t: t[1])
elif nowDir == 3:
	marbleList = sorted(marbleList, key=lambda t: t[1], reverse=True)
```

구슬을 굴려주는데, 벽이나 다른 구슬을 만날 때까지 굴린다.

구멍을 만난다면 구슬의 원래좌표는 없애준다. -> 빨간색 구슬이면 `redinHole`을 `True`로 변경, 파란색 구슬이면 `blueinHole`을 `True`로 변경

두 구슬이 모두 움직이지 않았거나, 파란색 공이 구멍안에 들어간 경우는 더 이상 게임을 진행하지 못하는 경우이기 때문에 재귀함수를 호출하지 않는다.

`now` == `goal`이 된 경우에 빨간공만 구멍에 들어간 상태가 된다면, 이 때의 `time`을 출력하고 끝낸다.



### :computer: Review

> 걸린 시간: 1시간 40분

흑 1시간 반안에 못했다 ㅜ ㅜ ㅜ ㅜ

파란색 공이 구멍으로 들어간 경우를 고려를 안해서,,, ㅠㅠ

빨간색공과 파란색공이 같이 들어간 경우만 생각했다 흑흑

좀 더 꼼꼼히 풀자