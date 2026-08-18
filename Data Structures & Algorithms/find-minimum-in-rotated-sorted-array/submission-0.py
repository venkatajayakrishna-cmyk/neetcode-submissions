class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        start = 0
        end = n - 1
        break_point = 0
        while start <= end:
            mid = start + (end - start) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                break_point = mid
                break
            elif mid < n - 1 and nums[mid] > nums[mid + 1]:
                break_point = mid +1
                break
            elif nums[start] <= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return nums[break_point]