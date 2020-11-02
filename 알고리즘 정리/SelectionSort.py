unsortedArr = [int(x) for x in input().split()]

print("**** Selection Sort ****")
for i in range(len(unsortedArr)):
    minIdx = unsortedArr.index(min(unsortedArr[i:]))
    unsortedArr[i], unsortedArr[minIdx] = unsortedArr[minIdx], unsortedArr[i]

    print("step{}: {}".format(i, unsortedArr))

