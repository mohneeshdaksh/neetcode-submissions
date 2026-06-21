class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                res1 = self.is_palindrome(s,left, right-1)
                res2 = self.is_palindrome(s, left+1, right)
                if any([res1, res2]):
                    return True
                else:
                    return False
            else:
                left += 1
                right -= 1
        return True

    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
