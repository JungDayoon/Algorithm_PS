unsortedArr = [int(x) for x in input().split()]

print("**** Insertion Sort ****")
step = 1
for i in range(1, len(unsortedArr)):
    compare = unsortedArr[i]
    j = i-1
    while j >= 0 and compare < unsortedArr[j]:
        unsortedArr[j+1] = unsortedArr[j]
        j -= 1
    unsortedArr[j+1] = compare
    print("step{}: {}".format(step, unsortedArr))
    step +=1

