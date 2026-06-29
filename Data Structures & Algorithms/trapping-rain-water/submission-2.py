class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        left_max, right_max = height[l], height[r]
        trapped_water = 0

        while l < r:
            if left_max <= right_max:
                l += 1
                curr_water = left_max - height[l]
                trapped_water += max(0, curr_water)
                left_max = max(left_max, height[l])
            else:
                r -= 1
                curr_water = right_max - height[r]
                trapped_water += max(0, curr_water)
                right_max = max(right_max, height[r])
        return trapped_water