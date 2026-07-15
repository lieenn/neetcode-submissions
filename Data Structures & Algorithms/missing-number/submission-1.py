class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalSum = 0

        for i in range(len(nums)+1):
            totalSum += i

        for n in nums:
            totalSum -= n

        return totalSum
        