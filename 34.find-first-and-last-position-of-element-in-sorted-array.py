#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30204
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (left+right)//2
            if target > nums[middle]:
                left = middle+1
            elif target < nums[middle]:
                right = middle - 1
            else:
                start = middle
                right = middle - 1
        end = -1
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (left+right)//2
            if target > nums[middle]:
                left = middle+1
            elif target < nums[middle]:
                right = middle - 1
            else:
                end = middle
                left = middle+1
        return [start, end]



# @lc code=end



#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#

