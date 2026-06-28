class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        total_water = 0

        for i in range(1, len(height)-1):
            left_max = max(height[:i])
            right_max = max(height[i+1:])

            if left_max <= height[i] or right_max <= height[i]:
                total_water += 0
            elif left_max > height[i] and right_max > height[i]:
                total_water += (min(left_max, right_max) - height[i])
        return total_water
