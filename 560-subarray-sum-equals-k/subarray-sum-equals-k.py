class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        t = 0
        c = 0
        mp = {0: 1}

        for x in nums:
            t += x

            if t - k in mp:
                c += mp[t - k]

            mp[t] = mp.get(t, 0) + 1

        return c
        