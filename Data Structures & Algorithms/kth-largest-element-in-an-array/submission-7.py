class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth = 0
        neg = []

        for n in nums:
            n = -1 * n
            neg.append(n)

        heapq.heapify(neg)

        while k > 0:
            kth = -1 * heapq.heappop(neg)
            k -= 1

        return kth

