class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = {}
        for task in tasks:
            freq_map[task] = freq_map.get(task, 0) + 1
        max_heap = [-count for count in freq_map.values()]
        heapq.heapify(max_heap)
        time = 0
        q = deque()     #(-cnt, idleTime)
        while max_heap or q:
            time += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time