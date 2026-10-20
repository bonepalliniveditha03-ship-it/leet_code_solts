from typing import List
from collections import Counter

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for i in range(0, n, k):
                arr = nums[i:i + k]
                expected = target[i:i + k]

                if Counter(arr) != Counter(expected):
                    valid = False
                    break

                drops = 0
                for j in range(k):
                    if arr[j] > arr[(j + 1) % k]:
                        drops += 1

                if drops > 1:
                    valid = False
                    break

            if valid:
                ans += k

        return ans