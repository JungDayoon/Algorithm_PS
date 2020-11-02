def quickSort(s, e, step):
    step += 1

    pivot = unsortedArr[s]  # 맨 앞의 value 로 설정
    bs = s
    be = e
    print("step{}: pivot: {}, arr: {}".format(step, pivot, unsortedArr))
    while s < e:
        while unsortedArr[e] >= pivot and s < e:
            e -= 1
        if s > e:
            break
        while unsortedArr[s] <= pivot and s < e:
            s += 1
        if s > e:
            break
        unsortedArr[s], unsortedArr[e] = unsortedArr[e], unsortedArr[s]

    unsortedArr[bs], unsortedArr[s] = unsortedArr[s], unsortedArr[bs]
    if bs < s:
        quickSort(bs, s-1, step)
    if be > e:
        quickSort(s+1, be, step)



unsortedArr = [int(x) for x in input().split()]
print("**** Quick Sort ****")
step = 0

quickSort(0, len(unsortedArr)-1, step)


