class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        h = sum(weights)
        while l<h:
            mid = (l+h)//2
            if canship(weights,days,mid):
                h = mid
            else:
                l = mid+1
        return l
def canship(weights,days,cap):
    days_needed = 1
    current = 0
    for weight in weights:
        if current + weight <= cap:
            current += weight
        else:
            days_needed += 1
            current = weight
    return days_needed <= days