class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        hash_map = {}
        for point in points:
            distance = ((point[0]**2) + (point[1]**2)) ** 0.5
            heap.append(distance)
            if distance not in hash_map:
                hash_map[distance] = [point]
            else:
                hash_map[distance].append(point)
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            pt = heapq.heappop(heap)
            res.append(hash_map[pt].pop())
        return res
