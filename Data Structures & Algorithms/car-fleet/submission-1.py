class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        for i in range(len(position)):
            pairs.append([position[i], speed[i]])
        pairs.sort(key=lambda x:x[0], reverse=True)
        print(pairs)
        
        for pos, sp in pairs:
            time = (target - pos) / sp
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
