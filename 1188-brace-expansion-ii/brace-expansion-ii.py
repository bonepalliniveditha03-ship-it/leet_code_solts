class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def solve(s, i):
            result = set()
            current = {""}

            while i < len(s) and s[i] != '}':
                
                if s[i] == '{':
                    inside, i = solve(s, i + 1)
                    
                    new_current = set()
                    for a in current:
                        for b in inside:
                            new_current.add(a + b)
                    
                    current = new_current

                elif s[i] == ',':
                    result.update(current)
                    current = {""}
                    i += 1

                else:
                    new_current = set()
                    for a in current:
                        new_current.add(a + s[i])
                    
                    current = new_current
                    i += 1

            result.update(current)

            if i < len(s) and s[i] == '}':
                i += 1

            return result, i

        answer, _ = solve(expression, 0)

        return sorted(answer)
        