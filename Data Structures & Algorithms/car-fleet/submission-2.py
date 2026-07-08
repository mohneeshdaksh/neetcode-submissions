class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, sp in pairs:
            time = (target - pos) / sp
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
