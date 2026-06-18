class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_in_set = set(nums)
        max_len = 0
        for i in nums_in_set:
            if (i-1) not in nums_in_set:
                length = 1
                while (i+length) in nums_in_set:
                    length += 1
                max_len = max(max_len, length)
            else:
                continue
        return max_len