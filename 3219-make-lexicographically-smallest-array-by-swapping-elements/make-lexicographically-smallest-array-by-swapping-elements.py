class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n=len(nums)
        pair=sorted((nums[i],i)for i in range(n))
        ans=nums[:]
        i=0
        while i<n:
            j=i
            while j+1<n:
                if pair[j+1][0]-pair[j][0]<=limit:
                    j+=1
                else:
                    break
            num = sorted(pair[k][1] for k in range(i,j+1))
            for k in range(i,j+1):
                ans[num[k-i]]=pair[k][0]
            i=j+1
        return ans