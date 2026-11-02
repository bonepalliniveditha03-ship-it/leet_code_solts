class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = len(nums) // 2
        median = nums[mid]

        ans = 0
        for num in nums:
            ans += abs(num - median)

        return ans