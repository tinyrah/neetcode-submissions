class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for ind, num in enumerate(nums):
            difference_to_look_for = target - num
            if difference_to_look_for in prevMap:
                return [prevMap[difference_to_look_for], ind]
            prevMap[num] = ind