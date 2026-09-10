class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ps = 0
        r_map = {0:-1}
        for i,num in enumerate(nums):
            ps += num
            remainder = ps%k
            if remainder in r_map:
                indx = i - r_map[remainder]
                if indx >= 2:
                    return True
            else:
                r_map[remainder] = i
        return False

        