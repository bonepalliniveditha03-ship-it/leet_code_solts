# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1,-1]
        prev = head
        current = head.next
        posi = 1
        critical_point1=-1
        critical_point2=-1
        minDistance=float('inf')

        while current.next:
            local_max = current.val > prev.val and current.val > current.next.val
            local_min = current.val < prev.val and current.val < current.next.val
            if local_max or local_min:
                if critical_point1 == -1:
                    critical_point1 = posi
                else:
                    minDistance=min(minDistance,posi-critical_point2)
                critical_point2 = posi
            prev = current
            current = current.next
            posi += 1
        if critical_point1 == critical_point2:
            return [-1,-1]
        maxDistance = critical_point2-critical_point1
        return [minDistance,maxDistance]
            
        