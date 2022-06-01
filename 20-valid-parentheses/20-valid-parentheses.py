class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        _dict = {"]":"[", "}":"{", ")":"("}
        for i in s:
            if i in _dict.values():
                stack.append(i)
            elif i in _dict.keys():
                if stack == [] or _dict[i] != stack.pop():
                    return False
            else:
                return False
        return stack == []
        