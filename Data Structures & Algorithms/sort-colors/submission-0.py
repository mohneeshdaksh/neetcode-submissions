class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_freq = {0:0,1:0,2:0}
        for i in nums:
                color_freq[i] += 1
        
        index = 0
        for j in range(color_freq[0]):
            nums[index] = 0
            index += 1
        for k in range(color_freq[1]):
            nums[index] = 1
            index += 1
        for l in range(color_freq[2]):
            nums[index] = 2
            index += 1
        