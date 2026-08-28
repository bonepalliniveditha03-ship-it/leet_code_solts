class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        x = val

        for i in range(len(nums)):
            if nums[i] != x:
                nums[k] = nums[i]
                k += 1

        return k
        