class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_s1 = {}
        dict_s2 = {}
        l, r = 0, len(s1) - 1
        for char in s1:
            dict_s1[char] = dict_s1.get(char, 0) + 1        
        while r < len(s2):
            if l == 0:
                for ch in range(l, r+1):
                    dict_s2[s2[ch]] = dict_s2.get(s2[ch], 0) + 1
            else:
                dict_s2[s2[r]] = dict_s2.get(s2[r], 0) + 1
            if dict_s1 == dict_s2:
                return True
            else:
                dict_s2[s2[l]] -= 1
                if dict_s2[s2[l]] == 0:
                    dict_s2.pop(s2[l])
                l += 1
                r += 1
        return False