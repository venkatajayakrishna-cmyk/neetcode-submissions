class Solution:
    def partition(self, nums):
        pivot = nums[-1]
        n = len(nums)
        l = []
        m = []
        r = []

        for i in range(n):
            if nums[i] > pivot:
                l.append(nums[i])
            elif nums[i] == pivot:
                m.append(nums[i])
            else:
                r.append(nums[i])
        
        return l, m, r

    def findKthLargest(self, nums: List[int], k: int) -> int:
        while True:
            l, m, r = self.partition(nums)

            if k <= len(l):
                nums = l
            
            elif k <= len(l) + len(m):
                return m[0]
            
            else:
                nums = r
                k = k - len(l) - len(m)