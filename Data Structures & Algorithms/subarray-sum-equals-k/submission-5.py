class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = { 0:1 }
        curr = 0 
        res = 0

        for i in nums:
            curr += i
            diff = curr - k
            
            res += prefix_sum.get(diff, 0)

            prefix_sum[curr] = 1 + prefix_sum.get(curr, 0)

        return res
