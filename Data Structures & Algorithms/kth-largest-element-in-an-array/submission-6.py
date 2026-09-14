class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg = []
        res = []

        for n in nums:
            neg.append(-1 * n)
        heapq.heapify(neg)

        while k > 0:
            n = -1 * heapq.heappop(neg)
            res.append(n)
            k -= 1
        return n