def heapify(idx, n):
    l = idx * 2 # left
    r = idx * 2 + 1
    s_idx = idx
    if l <= n and heap[s_idx] > heap[l]:
        s_idx = l
    if r <= n and heap[s_idx] > heap[r]:
        s_idx = r
    if s_idx != idx:
        heap[s_idx], heap[idx] = heap[idx], heap[s_idx]
        return heapify(s_idx, n)


def heapSort():
    n = len(heap)-1

    # min heap 생성
    for i in range(n, 0, -1):
        heapify(i, n)

    # min element extract and heapify
    for i in range(n, 0, -1):
        print(heap[1])
        heap[i], heap[1] = heap[1], heap[i]
        heapify(1, i-1)



heap = [int(x) for x in input().split()]
heap.insert(0, 0)

print("**** Heap Sort ****")
step = 0

heapSort()


