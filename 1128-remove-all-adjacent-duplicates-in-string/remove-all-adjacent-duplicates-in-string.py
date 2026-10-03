class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch: # if stack (not empty) if not stack(empty)
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
        
        