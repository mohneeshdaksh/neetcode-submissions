class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        onlyUnique = set()
        for i in nums:
            if i in onlyUnique:
                return True
            else:
                onlyUnique.add(i)
        return False