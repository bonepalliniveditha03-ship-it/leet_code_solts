class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = [len(s)] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        candidates = []

        for c in range(26):
            if first[c] == len(s):
                continue

            l = first[c]
            r = last[c]
            i = l
            valid = True

            while i <= r:
                x = ord(s[i]) - ord('a')

                if first[x] < l:
                    valid = False
                    break

                r = max(r, last[x])
                i += 1

            if valid:
                candidates.append((l, r))
        candidates.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for l, r in candidates:
            if l > prev_end:
                ans.append(s[l:r + 1])
                prev_end = r

        return ans
        