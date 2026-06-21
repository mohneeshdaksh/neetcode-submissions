class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < len(nums):
            if nums[i] < 1 or nums[i] > n or nums[i] == i+1 or nums[i]==nums[nums[i]-1]:
                i += 1
            else:
                target = nums[i]-1
                nums[i], nums[target] = nums[target], nums[i]
        for j in range(len(nums)):
            if nums[j] != j+1:
                return j+1
        return n+1
