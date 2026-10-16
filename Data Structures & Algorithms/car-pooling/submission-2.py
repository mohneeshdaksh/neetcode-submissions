class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_distance = max(trip[2] for trip in trips)
        dp = [capacity] * (max_distance + 1)
        for trip in trips:
            for index in range(trip[1],trip[2]):
                dp[index] -= trip[0]
                if dp[index] < 0:
                    return False
        return True