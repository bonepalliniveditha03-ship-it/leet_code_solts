class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minimum=0
        maximum=0
        for i in range(len(nums)):
            if nums[i]<nums[minimum]:
                minimum=i
            if nums[i]>nums[maximum]:
                maximum=i
        if minimum>maximum:
            minimum,maximum=maximum,minimum
        front = maximum+1
        back=len(nums)-minimum
        frnt_and_back=minimum+1+len(nums)-maximum
        return min(front,back,frnt_and_back)

        