class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minNum = nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                minNum = min(minNum, nums[l])

            m = (l + r) // 2
            minNum = min(minNum, nums[m])

            if nums[l] > nums[m]:
                r = m - 1
            else:
                l = m + 1

        return minNum
