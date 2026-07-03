class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            found = False
            days = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    days = j-i
                    result.append(days)
                    found = True
                    break
            if not found:
                result.append(days)
        return result

