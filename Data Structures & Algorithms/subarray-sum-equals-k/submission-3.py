class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = { 0:1 }
        sum = 0 
        res = 0

        for i in nums:
            sum += i
            diff = sum - k
            if diff in prefix_sum:
                res += prefix_sum.get(diff, 0)
            if sum in prefix_sum:
                prefix_sum[sum] += 1
            else:
                prefix_sum[sum] = 1
        return res
