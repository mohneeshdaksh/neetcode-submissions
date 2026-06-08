class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            for j in strs[1:]:
                if len(j) <= i:
                    return prefix
                elif j[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix