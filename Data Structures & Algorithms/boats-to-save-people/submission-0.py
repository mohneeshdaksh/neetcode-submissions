class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        l, r = 0, len(people)-1
        total_boats = 0

        while l <= r:
            if l == r:
                total_boats += 1
                l += 1
            elif people[l]+people[r] > limit:
                total_boats += 1
                r -= 1
            elif people[l]+people[r] <= limit:
                total_boats += 1
                l += 1
                r -= 1
        return total_boats