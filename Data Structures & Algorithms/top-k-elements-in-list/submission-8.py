class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        topK = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                topK.append(n)
                if len(topK) == k:
                    return topK

