class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_not_equal_to_val = 0

        ans = []
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

            