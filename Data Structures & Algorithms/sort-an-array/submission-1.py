class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    
        def merge(arr1,arr2):
            combined_arr = []
            p1, p2 = 0, 0

            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] < arr2[p2]:
                    combined_arr.append(arr1[p1])
                    p1 += 1
                else:
                    combined_arr.append(arr2[p2])
                    p2 += 1
            combined_arr += arr1[p1:]
            combined_arr += arr2[p2:]
            return combined_arr

        def merge_sort(nums):
            if len(nums) == 1:
                return nums
            else:
                mid = len(nums) // 2
                arr1 = nums[:mid]
                arr2 = nums[mid:]

                sorted_left = merge_sort(arr1)
                sorted_right = merge_sort(arr2)
            return merge(sorted_left, sorted_right)
        return merge_sort(nums)