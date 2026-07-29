class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lower = max(weights)
        upper = sum(weights)
        while lower < upper:
            cap = (lower + upper) // 2

            curr_days = 1
            curr_load = 0
            for w in weights:
                if curr_load + w > cap:
                    curr_days += 1
                    curr_load = 0
                curr_load += w

            if curr_days > days:
                lower = cap + 1
            elif curr_days <= days:
                upper = cap
        return upper