class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=0
        l=0
        n=len(nums)
        r=k-1
        for i in range(k):
            summ+=nums[i]
        maxi=summ/k
        while r<n-1:
            summ-=nums[l]
            l+=1
            r+=1
            summ+=nums[r]
            maxi=max(maxi,summ/k)
        return maxi
        