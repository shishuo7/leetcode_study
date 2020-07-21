# 26. 删除排序数组中的重复项
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        repeat_index = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[repeat_index] = nums[i]
                repeat_index += 1
        return repeat_index
