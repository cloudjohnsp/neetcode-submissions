class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        parentheses = {'[': ']', '{': '}', '(': ')'}
        for i in s:
            if i == '[' or i == '{' or i == '(':
                stack.append(parentheses[i])
            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack.pop() != i:
                        return False
        return True if len(stack) == 0 else False           