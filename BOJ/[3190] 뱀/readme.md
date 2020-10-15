# [BOJ 3190] 뱀

### :computer: Algorithm

> 덱, 구현



### :computer: Logic

`snake`: 뱀이 차지하는 좌표를 가지는 deque

`Map`: 지도를 2차원 리스트로 나타냄. 

좌표값이 -1인 경우: 벽이거나 뱀이 차지하고 있는 곳

좌표값이 0인 경우: 아무것도 없는 칸

좌표값이 1인 경우: 사과가 있는 칸

뱀의 머리: `snake[len(snake)-1]`

뱀의 꼬리: `snake[0]`

뱀이 이동할 때는, 새로운 좌표가 뱀의 머리가 되므로, `snake.append([new_y, new_x])`를 해준다.

뱀의 꼬리를 자를 때는, `snake.popleft()`를 통해서 구현할 수 있다.



### :computer: Review

> 걸린 시간: 45분

방향이 D, L일 때 현재 dir에서 +1, -1을 하는 방식으로 하니 dir이 엄청 커지거나 작아지는 경우가 있기 때문에 런타임에러가 떴다.

**수정코드**

```python
if changeInfo[process][1] == 'L':
	dir = (dir + 1) % 4
else:
	dir = (dir + 3) % 4
```

