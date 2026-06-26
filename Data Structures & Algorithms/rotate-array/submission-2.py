class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0] * len(nums)
        print(res)
        for i in range(len(nums)):
            kplace = (i+k) % len(nums)
            res[kplace] = nums[i]
        nums[:] = res