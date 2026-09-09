class Solution:
    def possible(self, min_weight, weights):
        sum_weights = 0
        count = 0
        for weight in weights:
            if sum_weights + weight <= min_weight:
                sum_weights += weight
            else:
                count += 1
                sum_weights = 0
                sum_weights += weight
        return count + 1

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        res = []

        while start <= end:
            mid = start + (end - start) // 2

            r_days = self.possible(mid, weights)
            if r_days > days:
                start = mid + 1
            else:
                res.append(mid)
                end = mid - 1
        return min(res)