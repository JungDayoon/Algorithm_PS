def merge(start, end, mid):
    global unsortedArr

    newArr = []
    i = start
    j = mid + 1

    while i <= mid and j <= end:
        if unsortedArr[i] < unsortedArr[j]:
            newArr.append(unsortedArr[i])
            i += 1
        else:
            newArr.append(unsortedArr[j])
            j += 1

    while i <= mid:
        newArr.append(unsortedArr[i])
        i += 1
    while j <= end:
        newArr.append(unsortedArr[j])
        j += 1

    newIdx = 0
    for c in range(start, end+1):
        unsortedArr[c] = newArr[newIdx]
        newIdx += 1


def mergeSort(start, end, step):
    if start < end:
        mid = (start + end) // 2
        step += 1
        mergeSort(start, mid, step)
        mergeSort(mid+1, end, step)

        merge(start, end, mid)
    print("step{}: {}".format(step, unsortedArr))


unsortedArr = [int(x) for x in input().split()]

print("**** Merge Sort ****")
step = 0

mergeSort(0, len(unsortedArr)-1, step)


