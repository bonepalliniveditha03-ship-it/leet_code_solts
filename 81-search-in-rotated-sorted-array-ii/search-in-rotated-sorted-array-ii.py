class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        L=0
        H=n-1
        while L<=H:
            mid=(L+H)//2
            if nums[mid]==target:
                return True

            if nums[L]==nums[mid]==nums[H]:
                L+=1
                continue
                
            if nums[L]<=nums[mid]:
                if nums[L]<=target and  target < nums[mid]:
                    H = mid-1
                else:
                    L = mid+1
            else:
                if nums[mid]<target and target <= nums[H]:
                    L=mid+1
                else:
                    H = mid-1  
        return False 

        
        