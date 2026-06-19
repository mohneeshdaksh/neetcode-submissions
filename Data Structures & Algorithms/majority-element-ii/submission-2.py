class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2 = 0,0
        element1, element2 = None, None
        
        for current_element in nums:
            if current_element == element1:
                count1 += 1
            elif current_element == element2:
                count2 += 1
            elif count1 == 0:
                element1 = current_element
                count1 += 1
            elif count2 == 0:
                element2 = current_element
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        ans = []
        min_count = len(nums) // 3
        actual_count1 = nums.count(element1)
        actual_count2 = nums.count(element2)
        if actual_count1 > min_count:
            ans.append(element1)
        if actual_count2 > min_count:
            ans.append(element2)

        return ans