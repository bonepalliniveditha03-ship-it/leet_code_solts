class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for n in range(left, right + 1):
            if all(i != '0' and n % int(i) == 0 for i in str(n)):
                ans.append(n)
        return ans
        