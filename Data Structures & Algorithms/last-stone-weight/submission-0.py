class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            pop1 = -heapq.heappop(heap)
            pop2 = -heapq.heappop(heap)
            if pop1 > pop2:
                heapq.heappush(heap, -(pop1-pop2))
        return -heap[0] if len(heap) > 0 else 0