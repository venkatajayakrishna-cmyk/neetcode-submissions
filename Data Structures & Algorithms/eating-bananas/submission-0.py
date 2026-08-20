class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        s = sum(piles)
        while start < end:
            mid = start + (end - start) // 2
            result = sum((x + mid - 1) // mid for x in piles)
            
            if result > h:
                start = mid + 1
            else:
                end = mid
        return end