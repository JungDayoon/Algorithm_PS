# [BOJ 15683] 감시 - Python

### :computer: Algorithm

> 브루트포스, 시뮬레이션



### :computer: Logic

`Map`: 사무실의 각 좌표가 어떤 상태인지를 나타내는 이차원 리스트

`CCTV`: cctv 종류에 따라 보는 방향의 경우의 수를 담고 있는 리스트

`cctvList`: 현재 cctv가 위치한 y좌표, x좌표, cctv 유형을 담은 리스트

cctvList를 돌면서 각 cctv유형에 맞는 방향을 다 해보면서 가장 많이 볼 수 있는 경우를 찾아야한다. -> 완전탐색



### :computer: Review

> 걸린 시간: 35분

처음에 count를 세는 방식으로 구현했었는데, 이러니까 겹치는 부분을 계속 빼주는 문제가 있어서 배열에 표시하는 방법으로 바꿨다. 처음부터 이렇게 했으면 더더 시간 단축할 수 있었는데 아쉽다 ..!!