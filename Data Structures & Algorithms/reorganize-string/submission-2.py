class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        freq = Counter(s)
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)
        if -(max_heap[0][0]) > (len(s)+1)//2:
            return ""
        prev = None
        while max_heap:
            count, char = heapq.heappop(max_heap)
            res.append(char)
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            if count+1 < 0:
                prev = (count+1, char)
        return ''.join(res)