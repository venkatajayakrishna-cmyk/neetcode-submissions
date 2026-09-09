class Solution:
    def possible(self, min_k, piles):
        count = 0
        for pile in piles:
            count += (pile + min_k - 1) // min_k
        return count

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        start = 1
        end = max(piles)

        min_k = float('inf')

        while start <= end:
            mid = start + (end - start) // 2

            r_hours = self.possible(mid, piles)
            if r_hours > h:
                start = mid + 1
            else:
                end = mid - 1
                min_k = min(min_k, mid)

        return min_k