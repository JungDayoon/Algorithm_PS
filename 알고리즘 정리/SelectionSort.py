unsortedArr = [int(x) for x in input().split()]

print("**** Selection Sort ****")
step = 1
for i in range(len(unsortedArr)):
    minIdx = unsortedArr.index(min(unsortedArr[i:]))
    unsortedArr[i], unsortedArr[minIdx] = unsortedArr[minIdx], unsortedArr[i]

    print("step{}: {}".format(step, unsortedArr))
    step += 1

