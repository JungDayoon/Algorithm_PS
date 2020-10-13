import sys

N = int(input())
card = [int(x+1) for x in range(N)]
trash = []
while len(card)>1:
    topCard = card.pop(0)
    trash.append(topCard)
    card.append(card.pop(0))

outputStr = ""
for i in range(len(trash)):
    outputStr += str(trash[i]) + " "

outputStr += str(card[0])
print(outputStr)

