class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # max_distance = max(trip[2] for trip in trips)
        # dp = [capacity] * (max_distance + 1)
        # for trip in trips:
        #     for index in range(trip[1],trip[2]):
        #         dp[index] -= trip[0]
        #         if dp[index] < 0:
        #             return False
        # return True
        
        trips.sort(key = lambda t: t[1])
        min_heap, curr_pass = [], 0
        for t in trips:
            num_pass, start, end = t
            while min_heap and min_heap[0][0] <= start:
                curr_pass -= min_heap[0][1]
                heapq.heappop(min_heap)
            curr_pass += num_pass
            if curr_pass > capacity:
                return False
            heapq.heappush(min_heap, [end, num_pass])
        return True