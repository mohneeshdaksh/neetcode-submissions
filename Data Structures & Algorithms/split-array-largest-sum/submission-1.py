class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        while l <= r:
            mid = (l + r) // 2

            total_k = 1
            total_sum = 0
            for num in nums:
                if total_sum + num > mid:
                    total_k += 1
                    total_sum = 0
                total_sum += num
            
            if total_k <= k:
                r = mid - 1
            else:
                l = mid + 1
        return l