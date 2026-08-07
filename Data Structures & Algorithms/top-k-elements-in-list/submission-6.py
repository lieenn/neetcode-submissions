class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count and keep track of every number
        # create a list[list] where the index is count & ele is the number
        # to find the top k numbers, find the first k number inside the list starting from the back

        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
        