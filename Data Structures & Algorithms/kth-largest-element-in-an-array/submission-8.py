class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = []
        for n in nums:
            heapq.heappush(largest, -1 * n)

        while k > 0:
            n = heapq.heappop(largest)
            k -= 1
        return -1 * n