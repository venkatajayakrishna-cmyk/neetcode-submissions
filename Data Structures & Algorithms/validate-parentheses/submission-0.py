class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}', '[':']'}
        stack = []
        for char in s:
            if char in brackets.keys():
                stack.append(char)
            if char in brackets.values():
                if stack:
                    last_opened = stack[-1]
                    if brackets[last_opened] != char:
                        return False
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False