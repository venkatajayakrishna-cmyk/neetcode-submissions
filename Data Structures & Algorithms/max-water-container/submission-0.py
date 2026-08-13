class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_water = 0
        res = []
        while l < r:
            if heights[l] < heights[r]:
                water = heights[l] * (r - l)
                res.append(water)
                l += 1
            else:
                water = heights[r] * (r - l)
                res.append(water)
                r -= 1 
        return max(res)