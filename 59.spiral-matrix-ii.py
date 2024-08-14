#
# @lc app=leetcode.cn id=59 lang=python3
# @lcpr version=30204
#
# [59] 螺旋矩阵 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        max_n = n * n
        num = 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        left, right, top, down = 0, n-1, 0, n-1
        while num<= max_n:
            if left ==right == top == down:
                mat[left][left] = num
                break
            for i in range(left, right):
                mat[top][i] = num
                num += 1
            top += 1
            for i in range(top-1, down):
                mat[i][right] = num
                num += 1
            right -= 1
            for i in range(right+1,left,-1):
                mat[down][i] = num
                num += 1
            down -= 1
            for i in range(down+1, top-1, -1):
                mat[i][left] = num
                num +=1
            left += 1
        return mat


            

# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

