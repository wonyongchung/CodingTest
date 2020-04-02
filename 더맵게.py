import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    while heap[0]<K:
        
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
