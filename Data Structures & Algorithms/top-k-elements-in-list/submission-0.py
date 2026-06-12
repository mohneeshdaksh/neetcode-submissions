class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        int_freq = {}
        for i in nums:
            if i in int_freq:
                int_freq[i] += 1
            else:
                int_freq[i] = 1
        sorted_freq = dict(sorted(int_freq.items(), key=lambda x:x[1], reverse=True))
        freq_element_count = 1
        freq_element_array = []
        for j in sorted_freq:
            if freq_element_count <= k:
                freq_element_array.append(j)
                freq_element_count += 1
            else:
                break
        return freq_element_array