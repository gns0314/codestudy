from heapq import heappush, heappop
def solution(operations):
    heap = []
    answer = []
    for i in operations:
        if i[0] == 'I':
            heappush(heap, i[2:])
        elif i[0] == 'D' and  i[2] == '-' and len(heap) != 0:
            min_num = str(min((map(int,heap))))
            heap.remove(min_num)
        elif i[0] == 'D' and  i[2] == '1' and len(heap) != 0:
            max_num = str(max((map(int,heap))))
            heap.remove(max_num)
    if len(heap) == 0:
        return [0,0]
    return [max((map(int,heap))),min((map(int,heap)))]