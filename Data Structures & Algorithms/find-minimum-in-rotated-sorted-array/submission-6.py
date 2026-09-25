class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[r] > nums[l]:
                minNum = min(minNum, nums[l])
                break

            m = (l + r) // 2
            minNum = min(minNum, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return minNum

        