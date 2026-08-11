class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for weight in stones:
            heapq.heappush(heap, -weight)
        
        while len(heap) > 1:
            first_stone = heapq.heappop(heap)
            second_stone = heapq.heappop(heap)

            if first_stone == second_stone:
                continue
            else:
                heapq.heappush(heap, -abs(first_stone - second_stone))
        if heap:
            return -heap[0]
        else:
            return 0