class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        kPoints = []
        for x, y in points:
            d = x**2 + y**2
            heapq.heappush(heap, [d, x, y])
        while k > 0:
            d, x, y = heapq.heappop(heap)
            kPoints.append([x,y])
            k -= 1
        return kPoints
       