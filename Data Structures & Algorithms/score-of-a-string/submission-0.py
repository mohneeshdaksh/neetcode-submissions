class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_arr = []
        score = 0
        for i in s:
            ascii_arr.append(ord(i))
        print(ascii_arr)
        for j in range(1, len(ascii_arr)):
            score = score + abs(ascii_arr[j] - ascii_arr[j-1])
        return score