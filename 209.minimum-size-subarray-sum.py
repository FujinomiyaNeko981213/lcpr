#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30204
#
# [209] 长度最小的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        sum = 0
        result = 0
        #精髓在于，当你找到一个符合条件的result之后，其他所有的结果都应该比这个result小，即保持i,j的相对位置
        for j in range(len(nums)):
            sum = sum + nums[j]
            while sum >= target:
                subl = j - i + 1
                if result>0:
                    result = min(result,subl)
                else:
                    result = subl
                sum = sum - nums[i]
                i = i + 1
        return result
# @lc code=end



#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#

