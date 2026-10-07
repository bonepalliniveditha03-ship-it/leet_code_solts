class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(x):
            count = 0

            for ch in x:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = deque([s])
        visited = {s}
        result = []
        found = False

        while queue:
            curr = queue.popleft()

            if isValid(curr):
                result.append(curr)
                found = True

            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in "()":
                    continue

                new_string = curr[:i] + curr[i + 1:]

                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

        return result
       
            