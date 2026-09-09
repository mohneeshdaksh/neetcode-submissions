class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        curr_sum = nums[l]
        min_len = len(nums) + 1
        answer_exist = False
        while r < len(nums):
            if curr_sum >= target:
                answer_exist = True
                min_len = min(min_len, (r-l+1))
                curr_sum -= nums[l]
                if l == r:
                    r += 1
                l += 1         
            elif curr_sum < target:
                r += 1
                if r == len(nums):
                    break
                curr_sum += nums[r]
        if answer_exist:
            return min_len
        else:
            return 0