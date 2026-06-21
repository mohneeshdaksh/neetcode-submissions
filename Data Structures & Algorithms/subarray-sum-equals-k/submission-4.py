class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = { 0:1 }
        sum = 0 
        res = 0

        for i in nums:
            sum += i
            diff = sum - k
            
            res += prefix_sum.get(diff, 0)

            prefix_sum[sum] = 1 + prefix_sum.get(sum, 0)

        return res
