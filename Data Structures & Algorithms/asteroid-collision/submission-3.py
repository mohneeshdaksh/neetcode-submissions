class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        remains = []
        remains.append(asteroids[0])
        for i in range(1, len(asteroids)):
            curr_survived = True
            while len(remains) != 0 and asteroids[i] < 0 and remains[-1] > 0:
                if remains[-1] == abs(asteroids[i]):
                    remains.pop()
                    curr_survived = False
                    break
                elif remains[-1] > abs(asteroids[i]):
                    curr_survived = False
                    break
                else:
                    remains.pop()
            if curr_survived == True:
                remains.append(asteroids[i])
        return remains