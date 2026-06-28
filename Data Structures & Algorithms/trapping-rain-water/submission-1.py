class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        total_water = 0
        precomputed_max = []
        
        for i in range(len(height)):
            if i == 0:
                precomputed_max.append([height[i],0])
            else:
                precomputed_max.append([max(precomputed_max[i-1][0],height[i-1]),0])
        for j in range(len(height)-1, -1, -1):
            if j == len(height)-1:
                precomputed_max[j][1] = height[j]
            else:
                precomputed_max[j][1] = max(precomputed_max[j+1][1], height[j+1])
        print(precomputed_max)

        for i in range(1, len(height)-1):
            if precomputed_max[i][0] <= height[i] or precomputed_max[i][1] <= height[i]:
                total_water += 0
            elif precomputed_max[i][0] > height[i] and precomputed_max[i][1] > height[i]:
                total_water += (min(precomputed_max[i][0], precomputed_max[i][1]) - height[i])
        return total_water
