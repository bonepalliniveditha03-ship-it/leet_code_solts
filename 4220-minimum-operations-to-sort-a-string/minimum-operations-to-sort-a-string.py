class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        sorunavile = s

        # Step 1: Check if the string is already sorted
        if s == ''.join(sorted(s)):
            return 0

        # Step 2: An unsorted string of length 2 cannot be sorted
        if n == 2:
            return -1

        # Step 3: Find the smallest and largest characters
        mn = min(s)
        mx = max(s)

        # Step 4: Check whether one operation is enough
        if s[0] == mn or s[-1] == mx:
            return 1

        # Step 5: Check the middle characters
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2

        # Step 6: Otherwise, three operations are needed
        return 3