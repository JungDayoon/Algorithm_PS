class photo:
    def __init__(self, num, count, index):
        self.num = num
        self.count = count
        self.index = index

    def __str__(self):
        return '({} {} {})'.format(self.num, self.count, self.index)

    def isEmpty(self):
        if self.num == -1 and self.count == 0 and self.index == -1:
            return True
        return False


N = int(input())
M = int(input())
candidate = [int(x) for x in input().split()]
frame = [photo(-1, 0, -1) for _ in range(N)]

for i, c in enumerate(candidate):
    print(i, c)
    for f in frame:
        if f.num == c:
            f.count += 1
            break
    else:  # 현재 사진틀에 이 학생이 없다면
        for f in frame:
            if f.isEmpty():
                f.num = c
                f.count = 1
                f.index = i
                break
        else:  # 사진틀에 빈 공간이 없다면
            frame = sorted(frame, key=lambda t: (t.count, t.index))
            frame[0].num = c
            frame[0].count = 1
            frame[0].index = i

for f in frame:
    print(f)

frameNum = map(lambda t: t.num, frame)
print(' '.join(map(str, sorted(frameNum))))

