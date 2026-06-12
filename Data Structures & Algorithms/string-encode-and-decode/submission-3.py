class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            str_len = str(len(i))
            s = s + str_len + "#" + i
        return s

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            del_index = s.find("#", i)
            string_len = int(s[i:del_index])
            i = del_index + string_len + 1
            str_captured = s[(del_index+1):i]
            decoded_str.append(str_captured)
        return decoded_str

            