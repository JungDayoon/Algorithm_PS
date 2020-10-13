import sys

tree = [int(x) for x in input().split()]
sortedTree = sorted(tree)

while True:
    for i in range(4):
        if(tree[i] > tree[i+1]):
            tree[i], tree[i+1] = tree[i+1], tree[i]
            outStr = ""
            for j in range(5):
                outStr += str(tree[j]) + " "
            print(outStr)
            
    if(tree == sortedTree):
        break
