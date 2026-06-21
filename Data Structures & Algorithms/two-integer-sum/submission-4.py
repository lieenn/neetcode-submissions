class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in found:
                return [found[complement], i]
            else:
                found[nums[i]] = i
        