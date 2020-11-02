unsortedArr = [int(x) for x in input().split()]

print("**** Bubble Sort ****")
step = 1
for c in range(len(unsortedArr)):
    for i in range(1, len(unsortedArr) - c):
        if unsortedArr[i] < unsortedArr[i-1]:
            unsortedArr[i], unsortedArr[i-1] = unsortedArr[i-1], unsortedArr[i]

    print("step{}: {}".format(step, unsortedArr))
    step += 1

