class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            ans.append(x * x)
        ans.sort()
        return ans