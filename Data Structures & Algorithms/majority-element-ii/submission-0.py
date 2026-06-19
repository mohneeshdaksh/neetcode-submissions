class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        min_count = len(nums) // 3
        seen = {}
        ans = []
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for j in seen:
            if seen[j] > min_count:
                ans.append(j)
        return ans