class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        total_len = len(word1) + len(word2)
        res = ["a" for _ in range(total_len)]
        first_pointer = 0
        second_pointer = 1
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            res[first_pointer] = word1[i]
            first_pointer += 2
        for j in range(min_len):
            res[second_pointer] = word2[j]
            second_pointer += 2
        third_pointer = min_len * 2
        remaining = word1[min_len:] + word2[min_len:]
        for k in range(len(remaining)):
            res[third_pointer] = remaining[k]
            third_pointer += 1
        return ''.join(char for char in res)