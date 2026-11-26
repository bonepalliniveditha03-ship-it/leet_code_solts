class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        turn = True

        while n >= stones:
            n -= stones
            stones -= 1
            turn = not turn

        return not turn