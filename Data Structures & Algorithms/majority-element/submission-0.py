class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic_ref = {}
        for i in nums:
            if i in dic_ref:
                dic_ref[i] += 1
            else:
                dic_ref[i] = 1
        min_len = len(nums) / 2
        for j in dic_ref:
            if dic_ref[j] > min_len:
                return j
            else:
                continue