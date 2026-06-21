class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = list("".join(char.lower() for char in s if char.isalnum()))
        left = 0
        right = len(clean_s)-1
        while left < right:
            if clean_s[left] == clean_s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True