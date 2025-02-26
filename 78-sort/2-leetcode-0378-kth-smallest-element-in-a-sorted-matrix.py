from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """ 二分查找 """

        def check(mid):
            n, m = len(matrix), len(matrix[0])
            r, c = n - 1, 0
            ans = 0
            while r >= 0 and c < m:
                if matrix[r][c] <= mid:
                    ans += r + 1  # 如果matrix[r][c]满足条件，那么该元素所在列在0~r行的元素都满足条件，总共r+1个元素
                    c += 1
                else:
                    r -= 1
            return ans >= k

        def lowerBound(left, right): # 寻找第一个大于等于k的元素
            while left <= right:
                mid = left + (right - left) // 2
                if check(mid):
                    right = mid - 1  # 左闭右闭
                else:
                    left = mid + 1
            return left

        left, right = matrix[0][0], matrix[-1][-1]
        return lowerBound(left, right)


if __name__ == '__main__':
    # matrix, k = [[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8
    matrix, k = [[-5]], 1
    print(Solution().kthSmallest(matrix, k))
