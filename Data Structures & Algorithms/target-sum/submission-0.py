class Solution:
    def TargetSum(self, nums, target, n):
        if n == 0:
            return 1 if target == 0 else 0
        
        if target - nums[n - 1] >= 0:
            return self.TargetSum(nums, target - nums[n - 1], n - 1) + self.TargetSum(nums, target, n - 1)
        else:
            return self.TargetSum(nums, target, n - 1)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total or (target + total) % 2 != 0:
            return 0

        n = len(nums)
        required_sum = (total + target) // 2
        
        t = [[0 for _ in range(required_sum + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(required_sum + 1):
                if i == 0:
                    t[i][j] = 1 if j == 0 else 0
                else:
                    if j - nums[i - 1] >= 0:
                        t[i][j] = t[i - 1][j - nums[i - 1]] + t[i - 1][j]
                    else:
                        t[i][j] = t[i - 1][j]
        return t[n][required_sum]