class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        total_elem = len(merged)
        
        if total_elem % 2 == 0:
            median = (merged[(total_elem//2)-1] + merged[total_elem//2])/2
            return median
        else:
            median = merged[total_elem//2]
            return median