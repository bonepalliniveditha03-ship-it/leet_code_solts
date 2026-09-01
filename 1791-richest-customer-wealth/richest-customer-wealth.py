class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        for row in accounts:
            maxi = max(maxi,sum(row))
        return maxi