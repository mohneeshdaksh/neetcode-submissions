class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = [(timestamp, value)]
        else:
            self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        l, r = 0, len(self.time_map[key]) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if self.time_map[key][mid][0] == timestamp:
                return self.time_map[key][mid][1]
            elif self.time_map[key][mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
            
            if r == -1:
                return ""
        return self.time_map[key][r][1]