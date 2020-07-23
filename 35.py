# 35. 搜索插入位置
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if target <= nums[i]:
        #         return i
        # return len(nums)
        if target > nums[-1]:
            return len(nums)
        left, right = 0, len(nums) -1
        while left < right:
            mid = (left + right) // 2
            # 下面判断耗时
            # if target == nums[mid]:
            #     return mid

            # 正确
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid

            # error 
            # if target < nums[mid]:
            #     right = mid - 1
            # else:
            #     left = mid
        return left