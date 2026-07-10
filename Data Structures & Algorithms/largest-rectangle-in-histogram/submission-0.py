class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            left = i
            right = i
            
            while left > 0:
                left -= 1
                if heights[left] < heights[i]:
                    left += 1
                    break
                    
            while right < len(heights)-1:
                right += 1
                if heights[right] < heights[i]:
                    right -= 1
                    break
            area = heights[i] * ((right-left)+1)
            max_area = max(area, max_area)
        return max_area