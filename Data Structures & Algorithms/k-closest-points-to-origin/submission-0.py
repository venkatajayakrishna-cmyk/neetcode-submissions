class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            heapq.heappush(heap, (((point[0]**2) + (point[1]**2)), point[0],        point[1]))
        
        result = []
        for _ in range(k):
            smallest = heapq.heappop(heap)
            result.append([smallest[1], smallest[2]])
        
        return result