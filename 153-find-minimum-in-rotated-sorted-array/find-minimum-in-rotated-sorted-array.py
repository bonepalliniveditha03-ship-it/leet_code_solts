class Solution:
    def findMin(self, nums: List[int]) -> int:
        L=0
        H=len(nums)-1
        while L<H:
            mid = (L+H)//2
            if nums[mid]>nums[H]:
                L = mid+1
            else:
                H = mid
        return nums[L]


        