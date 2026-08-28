class Solution:
    def findMin(self, nums: List[int]) -> int:
        L=0
        H=len(nums)-1
        while L<H:
            mid =(L+H)//2
            if nums[mid]>nums[H]:
                L=mid+1
            elif nums[mid]<nums[H]:
                H=mid
            else:
                H-=1
        return nums[L]