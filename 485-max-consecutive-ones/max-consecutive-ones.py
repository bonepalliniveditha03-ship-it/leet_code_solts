class Solutions:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        m = 0
        for num in nums:
            if num == 1:
                count += 1
                m = max(m, count)
            else:
                count = 0
        return m

        
