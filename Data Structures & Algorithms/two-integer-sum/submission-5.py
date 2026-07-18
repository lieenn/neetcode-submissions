class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in found:
                found[nums[i]] = i
            else:
                return [found[complement], i]
        