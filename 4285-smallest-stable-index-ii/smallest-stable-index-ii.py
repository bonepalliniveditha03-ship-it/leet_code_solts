class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix = [0] * n
        suffix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = min(nums[i], suffix[i + 1])
        maxi = nums[0]
        for i in range(n):
            maxi = max(maxi, nums[i])
            if maxi - suffix[i] <= k:
                return i
        return -1
        
        
        