class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = [(-count, char) for count, char in [(a, 'a'), (b, 'b'), (c, 'c')] if count > 0]
        heapq.heapify(max_heap)
        res = []
        while max_heap:
            count, char = heapq.heappop(max_heap)
            if len(res) > 1:
                if res[-1] == res[-2] == char:
                    blocked = (count, char)
                    if max_heap:
                        count, char = heapq.heappop(max_heap)
                        heapq.heappush(max_heap, blocked)
                    else:
                        break
            res.append(char)
            count += 1
            if count < 0:
                heapq.heappush(max_heap, (count, char))
        return ''.join(res)