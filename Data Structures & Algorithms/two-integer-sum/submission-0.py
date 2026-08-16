class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required = defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in required.keys():
                return [required[target - num], i]
            required[num] = i