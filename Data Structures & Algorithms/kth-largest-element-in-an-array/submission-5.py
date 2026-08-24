class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg_nums = []
        for n in nums:
            neg_nums.append(-1 * n)
        heapq.heapify(neg_nums)

        while k > 0:
            res = heapq.heappop(neg_nums)
            k -= 1

        return -1 * res

