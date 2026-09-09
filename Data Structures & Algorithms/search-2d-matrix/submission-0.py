class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)

        start = 0
        end = n - 1

        while start <= end:
            mid = start + ((end - start) // 2)

            r = matrix[mid]
            r_n = len(r)
            r_start = 0
            r_end = r_n - 1

            if r[r_start] <= target <= r[r_end]:
                while r_start <= r_end:
                    r_mid = r_start + ((r_end - r_start) // 2)

                    if r[r_mid] == target:
                        return True
                    elif r[r_mid] < target:
                        r_start = r_mid + 1
                    else:
                        r_end = r_mid - 1

                return False
            elif r[r_start] > target:
                end = mid - 1
            elif r[r_end] < target:
                start = mid + 1
        return False