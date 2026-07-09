class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []
        print(paths)
        for i in paths:
            if i == "..":
                if not stack:
                    continue
                else:
                    stack.pop()
            elif i == "" or i == ".":
                continue
            else:
                stack.append(i)
        output = ""
        for j in stack:
            output += "/" + j
        if not output:
            return "/"
        else:
            return output