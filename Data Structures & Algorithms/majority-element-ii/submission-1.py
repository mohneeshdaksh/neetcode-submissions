class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        count2 = 0
        element1 = None
        element2 = None
        for current_element in nums:
            if element1 is None:
                element1 = current_element
                count1 = 1
            elif element2 is None and current_element != element1:
                element2 = current_element
                count2 = 1
            elif current_element == element1:
                count1 += 1
            elif current_element == element2:
                count2 += 1
            elif current_element != element1 and current_element != element2:
                count1 -= 1
                count2 -= 1
                if count1 == 0:
                    element1 = None
                if count2 == 0:
                    element2 = None
        min_count = len(nums) // 3
        actual_count1 = nums.count(element1)
        actual_count2 = nums.count(element2)
        ans = []
        if actual_count1 > min_count:
            ans.append(element1)
        if actual_count2 > min_count:
            ans.append(element2)
        return ans