class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        r_map = {0: 1}
        ps = 0
        count = 0
        for i, num in enumerate(nums):
            ps += num
            remdr = ps % k
            if remdr in r_map:
                count += r_map[remdr]
                r_map[remdr] += 1
            else:
                r_map[remdr] = 1
        return count
        


        
        

        