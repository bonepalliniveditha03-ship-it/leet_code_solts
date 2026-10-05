class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                x = stack.pop()
                if x == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * x
        return stack[0]
        