class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_start = []
        prefix_end = []
        curr_sum = 0

        for num in nums:
            curr_sum += num
            prefix_start.append(curr_sum)

        curr_sum = 0

        for i in range(len(nums)-1, -1, -1):
            curr_sum += nums[i]
            prefix_end.append(curr_sum)
        
        prefix_end.reverse()
        
        for j in range(len(nums)):
            if prefix_start[j] == prefix_end[j]:
                return j
        
        return -1