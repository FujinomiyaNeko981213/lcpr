#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30204
#
# [54] 螺旋矩阵
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        all=n*m
        result = []
        left, right, top, down = 0, n-1, 0, m-1
        while True:
            for i in range(left, right+1):
                result.append(matrix[left][i])
                count += 1
                if count==all:return result
            top += 1
            for i in range(top, down+1):
                result.append(matrix[i][right])
                count += 1
                if count==all:return result
            right -=1
            for i in range(right, left-1,-1):
                result.append(matrix[down][i])
                count += 1
                if count==all:return result
            down -= 1
            for i in range(down, top-1, -1):
                result.append(matrix[i][left])
                count += 1
                if count==all:return result
            left += 1
            
            


# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

