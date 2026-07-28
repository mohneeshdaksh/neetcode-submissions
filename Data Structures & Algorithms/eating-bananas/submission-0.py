import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)
        bananas = sum(piles)
        while lower < upper:
            mid = (upper + lower) // 2
            curr_h = 0
            for pile in piles:
                curr_h += math.ceil(pile/mid)
            if curr_h > h:
                lower = mid + 1
            elif curr_h <= h:
                upper = mid
        return upper