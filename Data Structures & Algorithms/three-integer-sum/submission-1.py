class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        i = 0
        j = 1
        k = len(nums)-1
        res = []
        while i < len(nums)-2:
            three_sum = nums[i]+nums[j]+nums[k]
            if three_sum == 0:
                res.append([nums[i],nums[j],nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            elif three_sum > 0:
                k -= 1
            else:
                j += 1
            if j >= k:
                i += 1
                while i < len(nums)-2:
                    if nums[i] == nums[i-1]:
                        i += 1
                        continue
                    else:
                        break
                j = i+1
                k = len(nums)-1
        return res